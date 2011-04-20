#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/linkedlist.php

from pc import url

import re, urllib2

def step(n):
    u = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'
    out = urllib2.urlopen(u.format(n)).read()
    return out

# after a bunch of steps you get to 92118 and it tells you to divide by
# two and keep going
n = str(92118 / 2)

rx = re.compile(r'the next nothing is (\d+)')

try:
    while True:
        out = step(n)
        print 'out:', out
        n = rx.search(out).groups()[0]
        print 'next:', n

except KeyboardInterrupt:
    pass

# print the next level URL
print url.format('peak')
