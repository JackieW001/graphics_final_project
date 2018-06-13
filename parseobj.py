from display import *
from matrix import *
from math import *
from gmath import *
from draw import *
# -*- coding: utf-8 -*-


def get_face_list(f):
	file  = open(f, "r")

	vertexlist = []
	facelist = []


	linenumb = 1
	for line in file:
		listed_line = line.rstrip('\n').split(" ")
		cmd = listed_line[0]
		if cmd == "v":
			v = listed_line[1:]
			v = [float(x) for x in v]
			vertexlist.append(v)

		elif cmd == "f":
			args = listed_line[1:]
			args = [int(x) for x in args]
			face = []
			for i in args:
				face.append(vertexlist[i-1])
			facelist.append(face)

	return facelist


	


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
	'''
	print "====================="
	print face0
	print face1
	print face2
	print "====================="
	'''
	add_polygon(polygons, face0[0], face0[1], face0[2],face1[0], face1[1], face1[2],face2[0], face2[1], face2[2])


def add_faces(polygons, facelist):
	for face in facelist:
		if len(face) < 3:
			print "Too few points for face"
		else:
			for i in range(len(face)-2):
                                
			        if i == 0: 
				        polygon_adder(polygons, face[0],face[1],face[2])

				elif i == len(face)-3: 
					polygon_adder(polygons, face[2],face[i+2],face[0])

				else:
					polygon_adder(polygons, face[2],face[i+2],face[i+3])

	return polygons



'''
print "--------- VERTEXT LIST -----------"
print vertexlist
print "--------- POLYGON LIST -----------"
print facelist
'''
'''
polygons= []
x = get_face_list('test.txt')
print "+========= face list =========="
print x
print draw_faces(polygons, x)
'''
