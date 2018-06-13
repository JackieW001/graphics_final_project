from display import *
from matrix import *
from math import *
from gmath import *
from draw import *
# -*- coding: utf-8 -*-

file  = open("airboat.obj", "r")
lines = [line.rstrip('\n') for line in file]
#print lines

#Basic parsing through OBJ
vertexlist = []
facelist = []
for i in lines:
        cmd = i.split(" ")[0]
        if cmd == "v":
			v = [x for x in i.split()][1:]
			v = [float(x) for x in v]
			vertexlist.append(v)
        if cmd == "f":
			#print "===="
			args = [x for x in i.split()][1:]
			#print args
			f = [vertexlist[int(x)-1] for x in args]
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

#helper function 
def polygon_adder(polygons, face0, face1, face2):
	add_polygon(polygons, face0[0], face0[1], face0[2],
						  face1[0], face1[1], face1[2],
						  face2[0], face2[1], face2[2])

polygons = []
def draw_faces(polygons, facelist):
	for face in facelist:
		if len(face) < 3:
			print "Too few points for face"

		elif len(face) == 3:
			polygon_adder(polygons, face[0], face[1], face[2])

		elif len(face) == 4:
			polygon_adder(polygons, face[0], face[1], face[2])
			polygon_adder(polygons, face[0], face[2], face[3])

		elif len(face) == 5:
			polygon_adder(polygons, face[0], face[1], face[2])
			polygon_adder(polygons, face[2], face[3], face[4])
			polygon_adder(polygons, face[0], face[2], face[4])

		elif len(face) == 6:
			polygon_adder(polygons, face[0], face[1], face[2])
			polygon_adder(polygons, face[2], face[3], face[4])
			polygon_adder(polygons, face[2], face[4], face[5])
			polygon_adder(polygons, face[0], face[2], face[5])

		else:
			print "Faces has too many points"



'''
print "--------- VERTEXT LIST -----------"
print vertexlist
print "--------- POLYGON LIST -----------"
print facelist
'''

for face in facelist:
	print face[0]


