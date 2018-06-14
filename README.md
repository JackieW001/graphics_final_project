# 2018 Spring Final Graphics Project  

Period 4

Eric Li and Jackie Woo

### Running 
1. Install Xquartz
2. Clone this repo
3. Run `$make`
4. Your image will be generated (the default is an image of an airboat)

###  New Functionality  

1. OBJ Mesh Importing

   The graphics engine can now parse through and render .obj mesh images. 
   Simply put the command `mesh:<filename>` after your push and transformations.
   The `.obj` at the end of the filename should not be included.
   It will be in the same place where you draw other shapes such as circles or tori.

   Try out `airboat.mdl`!

2. Basic Shapes

   Four new shapes were added.
 
   * Cone                   `(x, y, z, radius, height)`
   * Cylinder               `(x, y, z, radius, height)`
   * Regular pyramid        `(x, y, z, width, height)`
   * Regular tetrahedron    `(x, y, z, edge length)`

   Edit the makefile and try out `newshape.mdl`!

### Note
Some things to note:
* The OBJ files should not have textures/vertex normals/shading commands. These commands are unnecessary since our graphics engine handles them already.
* The pyramid is generated from the peak downwards.

### Want to test out more OBJs?
Simply download files more OBJ files from [this link](https://people.sc.fsu.edu/~jburkardt/data/obj/obj.html).
Our graphics engine will render these files!
