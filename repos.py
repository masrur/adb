#!/usr/bin/env python3

# Print repository list

import datetime
import json

datafile = "repolist.json"

with open(datafile, 'r') as f:
    json_data = json.load(f)

repo_and_update_time = [
    (item["html_url"], datetime.datetime.strptime(item["updated_at"], '%Y-%m-%dT%H:%M:%SZ'), item["stargazers_count"])
    for item in json_data]

sorted_repo_list = sorted(repo_and_update_time, key=lambda x: x[1])

# Maximum length of repo URL
max_len_url = max([len(item[0]) for item in sorted_repo_list])

repo_str = "Repository URL"

print(repo_str, ' ' * (max_len_url - len(repo_str)), "Stargazers Count")
for item in sorted_repo_list:
    print(item[0], ' ' * (max_len_url - len(item[0])), item[2])
