# -*-coding:utf-8-*-

import json


def per_map_to_pro(data):
    per_map_pro_times = {}
    for item in data:
        per_map_pro_times[item['repo']['id']] = {}
    for item in data:
        per_map_pro_times[item['repo']['id']][item['actor']['id']] = {}
    for item in data:
        if item['type'] in ['PushEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent']:
            per_map_pro_times[item['repo']['id']][item['actor']['id']][item['type']] = per_map_pro_times[item['repo']['id']][item['actor']['id']].get(item['type'], 0) + 1
        per_map_pro_times[item['repo']['id']][item['actor']['id']]['PushEvent'] = per_map_pro_times[item['repo']['id']][item['actor']['id']].get("PushEvent", 0)
        per_map_pro_times[item['repo']['id']][item['actor']['id']]['IssueCommentEvent'] = per_map_pro_times[item['repo']['id']][item['actor']['id']].get("IssueCommentEvent", 0)
        per_map_pro_times[item['repo']['id']][item['actor']['id']]['IssuesEvent'] = per_map_pro_times[item['repo']['id']][item['actor']['id']].get("IssuesEvent", 0)
        per_map_pro_times[item['repo']['id']][item['actor']['id']]['PullRequestEvent'] = per_map_pro_times[item['repo']['id']][item['actor']['id']].get("PullRequestEvent", 0)
    return per_map_pro_times


def project_action_times(data):
    project_times = {}
    for item in data:
        if not isinstance(project_times.get(item["repo"]['id'], None), dict):
            project_times[item["repo"]['id']] = {}
        if item['type'] in ['PushEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent']:
            project_times[item["repo"]['id']][item['type']] = project_times[item["repo"]['id']].get(item['type'], 0) + 1
    for key in list(project_times.keys()):
        project_times[key]['PushEvent'] = project_times[key].get('PushEvent', 0)
        project_times[key]['IssueCommentEvent'] = project_times[key].get('IssueCommentEvent', 0)
        project_times[key]['IssuesEvent'] = project_times[key].get('IssuesEvent', 0)
        project_times[key]['PullRequestEvent'] = project_times[key].get('PullRequestEvent', 0)
    return project_times


def personal_action_times(data):
    personal_times = {}
    for item in data:
        if not isinstance(personal_times.get(item["actor"]['id'], None), dict):
            personal_times[item["actor"]['id']] = {}
        if item['type'] in ['PushEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent']:
            personal_times[item["actor"]['id']][item['type']] = personal_times[item["actor"]['id']].get(item['type'], 0) + 1
    for key in list(personal_times.keys()):
        personal_times[key]['PushEvent'] = personal_times[key].get('PushEvent', 0)
        personal_times[key]['IssueCommentEvent'] = personal_times[key].get('IssueCommentEvent', 0)
        personal_times[key]['IssuesEvent'] = personal_times[key].get('IssuesEvent', 0)
        personal_times[key]['PullRequestEvent'] = personal_times[key].get('PullRequestEvent', 0)
    return personal_times


def load_data():
    with open("./data.json", 'r+', encoding='utf-8') as fp:
        data = [json.loads(line) for line in fp.readlines()]
    return data


def save_data(data, filename=None):

    with open(filename, 'w+', encoding='utf-8') as fp:
        json.dump(data, fp, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    data = load_data()
    save_data(per_map_to_pro(data), "per_map_to_pro.json") # 每一个人在每一个项目的 4 种事件的数量。
    save_data(personal_action_times(data), "personal_action_times.json") #个人的 4 种事件的数量。
    save_data(project_action_times(data), "project_action_times.json") # 每一个项目的 4 种事件的数量。
