test: robot.mdl lex.py main.py matrix.py mdl.py display.py draw.py gmath.py yacc.py
	python2 main.py shapetest.mdl
	mv shape shape.ppm
	open shape.ppm
	
	

clean:
	rm *pyc *out parsetab.py
	rm *ppm

clear:
	rm *pyc *out parsetab.py *ppm

