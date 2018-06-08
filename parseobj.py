from display import *
from matrix import *
from math import *
from gmath import *
# -*- coding: utf-8 -*-

file  = open("test.txt", "r")
lines = [line.rstrip('\n') for line in file]

vertexlist = []
facelist = []
for i in lines:
        cmd = i[0]
        if cmd == "v":
                v = [x for x in i.split()][1:]
                v = [float(x) for x in v]
		vertexlist.append(v)
        if cmd == "f":
                args = [x for x in i.split()][1:]
                f = [vertexlist[int(x)] for x in args]
                facelist.append(f)
                

print "--------- VERTEXT LIST -----------"
print vertexlist
print "--------- POLYGON LIST -----------"
print facelist

