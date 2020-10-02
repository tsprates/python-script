#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python test
# author: Thiago <tsprates@gmail.com>

import json

managers = {}
watchers = {}

with open('source_file_2.json') as json_file:
    # load the json file
    data = json.load(json_file)

    # order by priority ascending
    sorted_data = sorted(data, key=lambda k: k['priority'], reverse=False)

    for item in sorted_data:
        for manager in item['managers']:
            managers[manager] = list()
        
        for watcher in item['watchers']:
            watchers[watcher] = list()

    for item in sorted_data:
        for manager in item['managers']:
            if not item['name'] in managers[manager]:
                managers[manager].insert(0, item['name'])
        
        for watcher in item['watchers']:
            if not item['name'] in watchers[watcher]:
                watchers[watcher].insert(0, item['name'])

# saves the managers
with open('managers.json', 'w') as managers_file: 
    managers_file.write(json.dumps(managers))

# saves the watchers
with open('watchers.json', 'w') as watchers_file:
    watchers_file.write(json.dumps(watchers))
