# -*- coding: utf-8 -*-

file  = open("test.txt", "r")
lines = [line.rstrip('\n') for line in file]

grouplist = []
vertexlist = []
for vertex in lines:
	if vertex == "g":
		grouplist.append(vertexlist)
		vertexlist = []
	else:	
		v = []
		v.append(vertex.split()[1])
		v.append(vertex.split()[2])
		v.append(vertex.split()[3])
		vertexlist.append(v)
		#print vertexlist

grouplist.append(vertexlist)
print grouplist
