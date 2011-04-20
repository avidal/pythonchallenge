#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/map.html

from pc import url

import string

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# this isn't the completely correct translation table, but it works
trans = string.maketrans(string.lowercase, ''.join([chr(ord(c)+2) for c in string.lowercase]))

print s.translate(trans)

print url.format('map'.translate(trans))
