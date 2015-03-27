from matrix_multiply import *
import numpy as np
from LU import *
import LU as LU
from solveHilbert import *
import fileinput
import sys


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
	f.write ("Solution: \n%s\n"%np.matrix(matrix))
	f.write ("Error: %s\n"%error)
	f.write("\n")

def createHilbertAndBMatrices(n):
	H = createHilbert(n)
	b = createB(n)
	return (H,b)

def doHilbert():
	f = open('output.txt','w')
	for n in range(2,21):
		(H,b) = createHilbertAndBMatrices(n)
		(l,u,y,x,e) = LU.doEverything(H,b)
		printPretty(n,x,e,f)
	f.close() 



# (l,u,y,x) = doEverything(H,b)
# print printPretty()