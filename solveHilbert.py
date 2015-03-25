from __future__ import print_function
from matrix_multiply import mult
import numpy as np
from LU import*
import fileinput


def createHilbert(n):
	H = [[0 for x in range(n)] for x in range(n)]
	for i in range(n):
		for j in range(n):
			H[i][j] = 1/float(i+j-1+2)
	return H		


def createB(n):
	value = np.math.pow(.1,float(n)/3)
	b = [[value] for x in range(n)]
	return b

def printPretty(n,matrix,error,f):
	f.write ("FOR N = %s:\n"%n);
	f.write ("Solution: %s\n"%matrix)
	f.write ("Error: %s\n"%error)
	f.write("\n")

def createHilbertAndBMatrices(n):
	H = createHilbert(n)
	b = createB(n)
	return (H,b)

def doHilbert():
	f = open('output.txt','w')
	for n in range(2,20):
		(H,b) = createHilbertAndBMatrices(n)
		(l,u,y,x,e) = doEverything(H,b)
		printPretty(n,x,e,f)
	f.close() 



#(l,u,y,x) = doEverything(H,b)
#print printPretty(x)