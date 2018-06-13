points = [0,1,2,3,4,5]


polygons=[]

for i in range(len(points)-2):
    print i
    triangle=[]
    if i == 0: # first triangle
        print "first tri"
        triangle.append(points[0])
        triangle.append(points[1])
        triangle.append(points[2])
    elif i == len(points)-3: #last triangle
        print "last tri"
        triangle.append(points[2])
        triangle.append(points[i+2])
        triangle.append(points[0])
    else:
        triangle.append(points[2])
        triangle.append(points[i+2])
        triangle.append(points[i+3])
    print triangle
    polygons.append(triangle)

print polygons
    
    
