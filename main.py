from script import run
import sys


### OBJ CHECKER
obj = False
if sys.argv[1].endswith('.obj'):
	obj = True
	


if len(sys.argv) == 2:
    run(sys.argv[1], obj)
elif len(sys.argv) == 1:
    run(raw_input("please enter the filename of an mdl script file: \n"))
else:
    print "Too many arguments."
