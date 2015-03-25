from matrix_multiply import mult
import numpy as np
from LU import computeLU

#i = columns
#j = rows
#matrix[row][col]


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
	U = [row[:] for row in L] #copy of b
	for i in range(len(L)/2):
		for j in range(len(L)):
			tempVector = U[len(U)-1-i]
			U[len(U)-i-1] = U[i] 
			U[i] = tempVector
	for i in range(len(L)/2):
		for j in range(len(L)):
			tempVal = U[j][i]
			U[j][i] = U[j][len(U)-i-1]
			U[j][len(U)-i-1] = tempVal
	return U

#Ux=y solves for x
def findX(U,y):
	size = len(U)
	x = [row[:] for row in y] #copy of b
	for i in range(size-1,-1,-1):
		for j in range(size-1,i,-1):
			x[i][0] -= U[i][j]*x[j][0]
		if (U[i][i]!=0):		
			x[i][0] /= U[i][i]
	return x

def flipMatrix(M):
	for i in range(len(M)/2):
		M[i][0],M[len(M)-i-1][0] = M[len(M)-i-1][0],M[i][0]  
	return M	

def doEverything(A,b):
	l,u = computeLU(A)
	convertedMatrix = convertToUpperTriangle(l)
	y = flipMatrix(findX(convertedMatrix,b))
	x = findX(u,y)

L = [[1,0,0],
	[2,1,0],
	[2,-1,1]]

U =	[[1,2,3],
	[0,2,1],
	[0,0,-1]]

# b=[[2],[1],[2]]


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

b = [[0.0464159],
	 [0.0464159],
	 [0.0464159],
	 [0.0464159]]

#given matrix L and U:
#convert the L to upper triangle
#solve Ly=b for y with findX and reversing it
#solve Ux=y for x with findX
# total = mult(l,u)
# print total
doEverything(h,b)
