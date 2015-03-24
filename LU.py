from matrix_multiply import mult
#from numpy import *
import numpy as np
#from sympy import Eq, Symbol, solve

#array[row][col]

def computeError(matrix):
	#add all elements in column. Absolute value it. Find the greatest value
	error = 0
	total = 0
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if (matrix[i][j] < 0):
				total-=matrix[i][j]
			else:
				total+=matrix[i][j]
		if(total>error):
			error = total			
		total = 0
	print (error," is the error")
	return error	

def getArrayToFindNorm(l,u,b):
	#returns (LU-H)
	return np.subtract(mult(l,u),b)

def computeLU(b):
	if(len(b)!=len(b[0])):
		print("The matrix must be nxn")
		return
	uMatrix = [row[:] for row in b] #copy of b
	lMatrix = [[0 for x in range(len(b))] for x in range(len(b))]
	for x in range(len(lMatrix)):
		lMatrix[x][x]=1
	startingValue = 1; #each time, increment
	for h in range(len(uMatrix)-1): #get zeros for each column. Do it for all h columns:
		print("starting h")
		for i in range(1+h,len(uMatrix)): #going down the row
			print("starting i")
			toScale = -1*(float)(uMatrix[i][h])/(uMatrix[h][h]); #value to multiply top row times
			valueOfL = -1*toScale
			#gets value of L matrix at current position 
			if(lMatrix[i][h]!=1):
				lMatrix[i][h] = valueOfL
			print("TOSCALE ",toScale)
			for j in range(h,len(uMatrix)): #move along cols
				print("starting j")
				uMatrix[i][j] = uMatrix[h][j]*toScale+uMatrix[i][j] #first [][] must be 0.
	print uMatrix
	print lMatrix
	return (lMatrix,uMatrix)


 
b =	[[2,4,-4],
	[1,-4,3],
	[-6,-9,5]];
(l,u) = computeLU(b)
array = getArrayToFindNorm(l,u,b) #gets (LU-H)	
error = computeError(b)

