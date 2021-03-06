#!/usr/bin/env python

import sys
import string

outdata = ''

def printitem(inputstring):
    global outdata
    name = inputstring.replace(' ', '_').lower()
    name = filter(lambda x: x in (string.lowercase + '_'), name)
    if inputstring[0] == ' ':
        inputstring = '"' + inputstring + '"'
    outdata += '<string name="' + name + '">' + inputstring + '</string>\n'

for line in iter(sys.stdin.readline, ""): 
    if (len(line) < 2):
        print outdata
        outdata = ''
    else:
        printitem(line.rstrip('\n'))

