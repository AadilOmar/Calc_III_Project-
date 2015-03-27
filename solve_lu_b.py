from matrix_multiply import *
import numpy as np
from LU import *
from solveHilbert import *
import fileinput
import sys




if (not hasArgument()):
	doHilbert()
	print "did hilbert"

else:	
	(A,B) = readFile()
	(l,u,y,x,e) = doEverything(A,B)
	f = open('output.txt','w')
	f.write ("L: \n%s\n\n"%np.array(l))
	f.write ("U: \n%s\n\n"%np.matrix(u))
	f.write ("x: \n%s\n\n"%np.matrix(x))
	f.write ("error: %s\n"%e)
	f.write("\n")
	f.close()
	print "did LU"
