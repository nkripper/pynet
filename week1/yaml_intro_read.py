#!/usr/bin/python

import yaml

with open("test_yaml.yml","r") as f:
	new_list = yaml.load(f)

print new_list

print yaml.dump(new_list)
