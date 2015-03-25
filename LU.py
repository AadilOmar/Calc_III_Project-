from matrix_multiply import mult
import numpy as np

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
		for i in range(1+h,len(uMatrix)): #going down the row
			if(uMatrix[h][h]==0):
				toScale = 1
			else:
				toScale = -1*(float)(uMatrix[i][h])/(uMatrix[h][h]); #value to multiply top row times
			valueOfL = -1*toScale
			#gets value of L matrix at current position 
			if(lMatrix[i][h]!=1):
				lMatrix[i][h] = valueOfL
			for j in range(h,len(uMatrix)): #move along cols
				uMatrix[i][j] = uMatrix[h][j]*toScale+uMatrix[i][j] #first [][] must be 0.
	#print uMatrix
	#print lMatrix
	return (lMatrix,uMatrix)


h= [[1,.5,.3333,.25],
	[.5,.3333,.25,.2],
	[.3333,.25,.2,.1666],
	[.25,.2,.1666,.1428]] 
b =	[[2,4,-4],
	[1,-4,3],
	[-6,-9,5]];
#(l,u) = computeLU(h)
#array = getArrayToFindNorm(l,u,h) #gets (LU-H)	
#error = computeError(h)

