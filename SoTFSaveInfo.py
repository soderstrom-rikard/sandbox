#!/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

from collections import OrderedDict

class SortedOrderedDict(OrderedDict):
    'Sort items in alphabetical order on insertion'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        for sorted_key in sorted(self.keys()):
            self.move_to_end(sorted_key)


def unescapeEmbededJson(s):
    return json.loads(''.join([*s]))


def readDirectoryOfJsonFiles(path):
    config = OrderedDict({ 'path': path })

    for file_name in os.listdir(path):
        if file_name.endswith('.json'):
            node_path = os.path.join(path, file_name)
            with open(node_path, 'r') as f:
                node = json.loads(f.read())

                for (node_key, node_value) in node.items():

                    if node_key == 'Data':
                        if node_key not in config:
                            config[node_key] = SortedOrderedDict()

                        for (k,v) in node[node_key].items():
                            v_json = unescapeEmbededJson(v)

                            if k in config[node_key] and v_json != config[node_key][k]:
                                raise Exception(f'Data {k} with value {v_json}, already set to value {config[node_key][k]}, aborting')

                            config[node_key][k] = v_json

                    else:
                        if node_key in config and node_value != config[node_key]:
                            raise Exception(f'{node_key} with value {node_value}, already set to value {config[node_key]}, aborting')

                        config[node_key] = node_value

    return config


config = readDirectoryOfJsonFiles('.config')
print("Save Info Configuration\n",json.dumps(config, indent=4))

currentSave = readDirectoryOfJsonFiles(
    os.path.join(
        config['input']['driveDir'],
        config['input']['savesDir'],
        config['input']['selectedSaveDir']
))
print(f"Loaded save {currentSave['path']}")

output_dir = os.path.join('.config', config['output']['outDir'])
output_file = os.path.join(output_dir, 'test.json')
os.makedirs(output_dir, exist_ok=config['output']['overwrite'])
with open(output_file , 'w') as f:
    f.write(json.dumps(currentSave, indent=4))
print(f"Saved decoded version at {output_file}")
