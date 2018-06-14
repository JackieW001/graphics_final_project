test: lex.py main.py matrix.py mdl.py display.py draw.py gmath.py yacc.py
	python2 main.py shapetest.mdl

	
	

clean:
	rm *pyc *out parsetab.py
	rm *ppm

clear:
	rm *pyc *out parsetab.py *ppm

