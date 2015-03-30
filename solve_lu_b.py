from matrix_multiply import *
import numpy as np
import LU as LU
from solveHilbert import *
import fileinput
import sys


def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False






if(isInt(sys.argv[1])):
	doHilbert(sys.argv[1])
else:
	(A,B) = LU.readFile(sys.argv[1])
	(l,u,y,x,e) = LU.lu_fact(A,B)
	f = open('output.txt','w')
	if(len(sys.argv)==3):
		f.write ("x: \n%s\n\n"%np.matrix(x))
		f.write ("error: %s\n"%e)
		#solve
	else:
		f.write ("L: \n%s\n\n"%np.array(l))
		f.write ("U: \n%s\n\n"%np.matrix(u))
		#return l,u	
	f.write("\n")
	f.close()	

	# (A,B) = LU.readFile()
	# # print A
	# # print B
	# (l,u,y,x,e) = LU.lu_fact(A,B)
	# # print x
	# f = open('output.txt','w')
	# f.write ("L: \n%s\n\n"%np.array(l))
	# f.write ("U: \n%s\n\n"%np.matrix(u))
	# # f.write ("x: \n%s\n\n"%np.matrix(x))
	# f.write ("error: %s\n"%e)

	# print "did LU"
