from display import *
from matrix import *
from math import *
from gmath import *
from draw import *
# -*- coding: utf-8 -*-

file  = open("test.txt", "r")
lines = [line.rstrip('\n') for line in file]

#Basic parsing through OBJ
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
          


#Parsing for polygons
#4
#		0
#	1		3
#		2	

# (0,1,2) (0,2,3)
#5
#		0
#	1		4
#	2		3

# (0,1,2) (2,3,4) (0,2,4)

polygons = []
def draw_faces(polygons, facelist):
	for face in facelist:
		if len(facelist[face]) < 3:
			print "Too few points for face"

		elif len(facelist[face][face]) == 3:
			add_polygon(polygons, facelist[face][0], facelist[face][1], facelist[face][2])

		elif len(facelist[face]) == 4:
			add_polygon(polygons, facelist[face][0], facelist[face][1], facelist[face][2])
			add_polygon(polygons, facelist[face][0], facelist[face][2], facelist[face][3])

		elif len(facelist[face]) == 5:
			add_polygon(polygons, facelist[face][0], facelist[face][1], facelist[face][2])
			add_polygon(polygons, facelist[face][2], facelist[face][3], facelist[face][4])
			add_polygon(polygons, facelist[face][0], facelist[face][2], facelist[face][4])

		elif len(facelist[face]) == 6:
			add_polygon(polygons, facelist[face][0], facelist[face][1], facelist[face][2])
			add_polygon(polygons, facelist[face][2], facelist[face][3], facelist[face][4])
			add_polygon(polygons, facelist[face][2], facelist[face][4], facelist[face][5])
			add_polygon(polygons, facelist[face][0], facelist[face][2], facelist[face][5])

		else:
			print "Faces has too many points"

print "--------- VERTEXT LIST -----------"
print vertexlist
print "--------- POLYGON LIST -----------"
print facelist




