#!/usr/bin/python

import json

my_list = range(9)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]['ip_addr'] = '10.10.10.239'
my_list[-1]['attribs'] = range(5)

print my_list

print json.dumps(my_list)

with open("test_json.json","w") as f:
	json.dump(my_list,f)
