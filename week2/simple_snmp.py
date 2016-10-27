#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP = '184.105.247.70'

# Creates a staic tuple.. cannt add or modify values
a_device = (IP, COMMUNITY_STRING, SNMP_PORT)

OID = '1.3.6.1.2.1.1.5.0'

# Gets the OID value.. what is very important here is that the value is
# returned in hexidecimal values and must be converted to a readable format
snmp_data = snmp_get_oid(a_device, oid=OID)

# This function will convert the SNMP data to a readable format by extracting
# the values.
output = snmp_extract(snmp_data)

print output
