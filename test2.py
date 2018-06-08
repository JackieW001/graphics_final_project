from draw import *


polygons = []
facelist= []


#3
if len(facelist) == 3:
	add_polygon(polygons, facelist[0], facelist[1], facelist[2])

#		0
#	1		3
#		2	

# (0,1,2) (0,2,3)

#4
if len(facelist) == 4:
	add_polygon(polygons, facelist[0], facelist[1], facelist[2])
	add_polygon(polygons, facelist[0], facelist[2], facelist[3])


#5
#		0
#	1		4
#	2		3

# (0,1,2) (2,3,4) (0,2,4)
if len(facelist) == 4:
	add_polygon(polygons, facelist[0], facelist[1], facelist[2])
	add_polygon(polygons, facelist[2], facelist[3], facelist[4])
	add_polygon(polygons, facelist[0], facelist[2], facelist[4])


#6
if len(facelist) == 4:
	add_polygon(polygons, facelist[0], facelist[1], facelist[2])
	add_polygon(polygons, facelist[2], facelist[3], facelist[4])
	add_polygon(polygons, facelist[2], facelist[4], facelist[5])
	add_polygon(polygons, facelist[0], facelist[2], facelist[5])