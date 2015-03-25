from matrix_multiply import mult
import numpy as np


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
	return error	

def getArrayToFindNorm(l,u,a):
	return np.subtract(mult(l,u),a)

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
	return (lMatrix,uMatrix)

def rowReduce(A,b):
	if(len(A)!=len(A[0])):
		print("The matrix must be nxn")
		return
	uMatrix = [row[:] for row in A] #copy of b
	for h in range(len(uMatrix)-1): #get zeros for each column. Do it for all h columns:
		for i in range(1+h,len(uMatrix)): #going down the row
			if(uMatrix[h][h]==0):
				toScale = 1
			else:
				toScale = -1*(float)(uMatrix[i][h])/(uMatrix[h][h]); #value to multiply top row times
			valueOfL = -1*toScale
			#gets value of L matrix at current position 
			for j in range(h,len(uMatrix)): #move along cols
				uMatrix[i][j] = uMatrix[h][j]*toScale+uMatrix[i][j] #first [][] must be 0.
	return (uMatrix)

def convertToUpperTriangle(L):
	# U = [row[:] for row in L] #copy of b
	U = list(L)
	for i in range(len(L)/2):
		for j in range(len(L)):
			tempVector = U[len(U)-1-i][j]
			U[len(U)-i-1][j] = U[i][j] 
			U[i][j] = tempVector
	for i in range(len(L)/2):
		for j in range(len(L)):
			tempVal = U[j][i]
			U[j][i] = U[j][len(U)-i-1]
			U[j][len(U)-i-1] = tempVal
	return U

def flipMatrix(M):
	M.reverse()
	# for i in range(len(M)/2):
	# 	M[i][0],M[len(M)-i-1][0] = M[len(M)-i-1][0],M[i][0]
	return M	

def findX(U,y):
	size = len(U)
	# x = [row[:] for row in y] #copy of b
	x = list(y)
	for i in range(size-1,-1,-1):
		for j in range(size-1,i,-1):
			x[i][0] -= U[i][j]*x[j][0]
		if (U[i][i]!=0):
			x[i][0] /= U[i][i]
	return x

def findY(L,b):
	print L
	newList = [[0 for x in range(len(L))] for x in range(len(L))]
	for i in range(len(L)):
		for j in range(len(L)):
			newList[i][j] = L[i][j]
	convertedMatrix = convertToUpperTriangle(newList)
	print L
	y = flipMatrix(findX(convertedMatrix,flipMatrix(b)))
	return y	 

def doEverything(A,b):
	l,u = computeLU(A)
	y = findY(l,b)
	x = findX(u,y)
	arr = getArrayToFindNorm(l,u,A)
	e = computeError(arr)
	return (l,u,y,x,e)


L = [[1,0,0],
	[2,1,0],
	[2,-1,1]]

U =	[[1,2,3],
	[0,2,1],
	[0,0,-1]]

A = [[1,2,2],
	 [0,1,4],
	 [0,0,2]]
B = [[2],
	 [2],
	 [2]]

l = [[1,0,0,0],
	 [.5,1,0,0],
	 [0.333333,1,1,0],
	 [.25,.9,1.5,1]]

u =	[[1,.5,.333333,.25],
	 [0,0.0833333,0.0833333, .075],
	 [0,0,0.00555556, 0.00833333],
	 [0, 0, 0, 0.000357143]]

h =	[[1,.5,.333333,.25],
	 [.5,.33333,.25, .2],
	 [.33333,.25, .2, 0.1666667],
	 [.25, .2, .1666667, .14285714]]	 
y = [[0.046415],
	 [0.0232075],
	 [9283/float(1200000)],
	 [0.00232075]]

b = [[0.0464159],
	 [0.0464159],
	 [0.0464159],
	 [0.0464159]]
