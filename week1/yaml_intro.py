#!/usr/bin/python

import yaml

my_list = range(8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]['ip_addr'] = '10.10.10.239'
my_list[-1]['attribs'] = range(7)

print my_list

print yaml.dump(my_list)

#yaml.dump(my_list,default_flow_style=True)

with open("test_yaml.yml","w") as f:
	f.write(yaml.dump(my_list))
