from matrix_multiply import mult
import numpy as np
from LU import *
from solveHilbert import *
import fileinput
import sys

def separateMatrices(matrix):
	num = np.math.sqrt(len(matrix))
	cols = int(np.math.floor(num))
	A = [[0 for x in range(cols)] for x in range(cols)]
	B = [[1 for x in range(1)] for x in range(cols)]
	print A
	print B
	# B = [1 for index in range(cols)]
	index = 0
	for i in range(cols):
		for j in range(cols):
			A[i][j] = matrix[index]
			index+=1
		if (not num.is_integer()):
			index+=1
	if (not num.is_integer()):
		anotherIndex = cols	
		for k in range(cols-1):
			anotherIndex+=(cols+1)
			B[k][0] = matrix[anotherIndex]
	return (A,B)

def hasArgument():
	if(len(sys.argv)==1):
		return False
	else:
		return True	

def readFile():
	total = "" 
	for line in fileinput.input():
		total+=line
	total = total.replace('\n',' ')	
	array = total.split(' ')
	array.pop()	
	for i in range(len(array)):
		array[i] = float(array[i])
	(a,b) = separateMatrices(array)	
	return (a,b)


if (not hasArgument()):
	doHilbert()
	print "did hilbert"

else:	
	(A,B) = readFile()
	(l,u,y,x,e) = doEverything(A,B)
	f = open('output.txt','w')
	f.write ("L: %s\n"%l)
	f.write ("U: %s\n"%u)
	f.write ("x: %s\n"%x)
	f.write ("error: %s\n"%e)
	f.write("\n")
	f.close()
	print "did LU"
