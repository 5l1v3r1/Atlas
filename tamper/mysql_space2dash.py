#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random

def mysql_space2dash(payload):
	# -- mysql -- #
	_payload = ""
	if payload:
		for i in xrange(len(payload)):
			if payload[i].isspace():
				randomStr = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase)
					for _ in xrange(random.randint(6,12)))
				_payload += "--%s%%0A"%randomStr
			elif payload[i] == '#' or payload[i:i + 3] == '-- ':
				_payload += payload[i:]
				break
			else:
				_payload += payload[i]
	return _payload