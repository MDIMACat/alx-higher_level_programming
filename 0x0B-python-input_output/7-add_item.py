#!/usr/bin/python3
"""Module to add items to JSON file"""
import sys


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    data = load(filename)
except FileNotFoundError:
    data = []

for arg in sys.argv[1:]:
    data.append(arg)

save(data, filename)
