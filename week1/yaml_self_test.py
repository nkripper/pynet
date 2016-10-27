#!/usr/bin/python

import yaml

router = {}

router['EUGNOR53CR81'] = {}
router['EUGNOR53CR81']['ipv4_address'] = '216.221.96.16'
router['EUGNOR53CR81']['eqpt_vendor'] = 'Nokia'

router['PTLDORPBCR81'] = {}
router['PTLDORPBCR81']['ipv4_address'] = '216.221.96.17'
router['PTLDORPBCR81']['eqpt_vendor'] = 'Nokia'

router['PTLDORPBCR82'] = {}
router['PTLDORPBCR82']['ipv4_address'] = '216.221.96.18'
router['PTLDORPBCR82']['eqpt_vendor'] = 'Nokia'

router['STTLWAWBCR81'] = {}
router['STTLWAWBCR81']['ipv4_address'] = '216.221.96.19'
router['STTLWAWBCR81']['eqpt_vendor'] = 'Nokia'

print yaml.dump(router)
