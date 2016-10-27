#!/usr/bin/python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

print cisco_cfg

print "-------------------"
print cisco_cfg.find_objects(r"^interface")

print "-------------------"
intf = cisco_cfg.find_objects(r"^interface")
for i in intf:
	print i.text

print "-------------------"
fa4 = intf[4]
print fa4

print "-------------------"
print fa4.children

print "-------------------"
for child in fa4.children:
	print child.text

print "-------------------"
print child.is_parent
print child.is_child

print "-------------------"
print "All IP Addresses that do not have an IP Address"
for child in cisco_cfg.find_objects_w_child(parentspec=r"^interface", childspec=r"no ip address"):
	print child.text

print "-------------------"
print "All IP Addresses that have an IP Address"
for child in cisco_cfg.find_objects_wo_child(parentspec=r"^interface", childspec=r"no ip address"):
	print child.text


