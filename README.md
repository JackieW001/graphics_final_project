# Final Graphics Project  

##To Do  

1. .OBJ Mesh Importing
* put verticies in list
* create face (aka polygon list) based on vertex indicies

2. Basic Shapes
* Cylinder - like torus without the rotating circle
* Cone - circles starting with radius r --> 0 over the course of height h
* Rectangular Pyramid - hard code



Main     
* Parse obj files     

Side     
* Add cone     
* Add cylinder     
* Add pyramid     
* Add other shapes          

Maybe
* Gouraud shading     
     

## Parsing Obj     
     
v = vertices (**float** coordinate, **float**, **float**)     
g = group name (optional **string**)     
s = smoothing group (**off/1**)      
f = face (**int** index of v1, **int**, **int**)     
