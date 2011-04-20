#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/peak.html

from pc import url

import cPickle as pickle

blob = pickle.loads(open('data/banner.p').read())

# the blob is a list of lists of pairs. the first item is a # or a space
# the second is an integer. because of the name banner, this is going
# to be printed

for line in blob:
    print ''.join(pair[0]*pair[1] for pair in line)

# the output looks like the word CHANNEL

# print the next level URL
print url.format('channel')
