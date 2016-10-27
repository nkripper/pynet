#!/usr/bin/python

import json

with open("test_json.json","r") as f:
	new_list = json.load(f)

print new_list
