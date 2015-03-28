from matrix_multiply import *
import numpy as np
from LU import *
from solveHilbert import *
import fileinput
import sys

def computeError(matrix):
	#add all elements in column. Absolute value it. Find the greatest value
	error = 0
	total = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if (matrix[i][j] < 0):
				total-=float(matrix[i][j])
			else:
				total+=float(matrix[i][j])
		if(total>error):
			error = total			
		total = 0
	return error	

def getArrayToFindNorm(l,u,a):
	return np.subtract(mMult(l,u),a)

def computeLU(b):
	if(len(b)!=len(b[0])):
		print("The matrix must be nxn")
		return
	uMatrix = [row[:] for row in b] #copy of b
	lMatrix = [[0.0 for x in range(len(b))] for x in range(len(b))]
	for x in range(len(lMatrix)):
		lMatrix[x][x]=1.0
	startingValue = 1; #each time, increment
	for h in range(len(uMatrix)-1): #get zeros for each column. Do it for all h columns:
		for i in range(1+h,len(uMatrix)): #going down the row
			if(uMatrix[h][h]==0.0):
				toScale = 1
			else:
				toScale = -1*(float)(uMatrix[i][h])/float(uMatrix[h][h]); #value to multiply top row times
			valueOfL = float(-1*toScale)
			#gets value of L matrix at current position 
			if(lMatrix[i][h]!=1):
				lMatrix[i][h] = valueOfL
			for j in range(h,len(uMatrix)): #move along cols
				uMatrix[i][j] = float(uMatrix[h][j])*toScale+float(uMatrix[i][j]) #first [][] must be 0.		
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
	# might have crashed LU- check over again to see if it still works
	# M.reverse()
	for i in range(len(M)/2):
		M[i][0],M[len(M)-i-1][0] = M[len(M)-i-1][0],M[i][0]
	return M	

def findX(U,y):
	size = len(U)
	x = [[0 for x in range(1)] for x in range(len(U))]
	for i in range(len(U)):
		x[i][0] = y[i][0]
	for i in range(size-1,-1,-1):
		for j in range(size-1,i,-1):
			x[i][0] -= (U[i][j])*(x[j][0])
		if (U[i][i]!=0):
			x[i][0] /= (U[i][i])
	return x

def findY(L,b):
	newList = [[0 for x in range(len(L))] for x in range(len(L))]
	for i in range(len(L)):
		for j in range(len(L)):
			newList[i][j] = L[i][j]		
	convertedMatrix = convertToUpperTriangle(newList)
	y = flipMatrix(findX(convertedMatrix,flipMatrix(b)))
	return y	 

def doEverything(A,b):
	# print A
	l,u = computeLU(A)
	y = findY(l,b)
	x = findX(u,y)
	arr = getArrayToFindNorm(l,u,A)
	e = computeError(arr)
	return (l,u,y,x,e)

def separateMatrices(matrix):
	
	num = np.math.sqrt(len(matrix))
	cols = int(np.math.floor(num))
	A = [[0 for x in range(cols)] for x in range(cols)]
	B = [[1 for x in range(1)] for x in range(cols)]
	index = 0
	for i in range(cols):
		for j in range(cols):
			A[i][j] = float(matrix[index])
			index+=1
		if (not num.is_integer()):
			index+=1
	if (not num.is_integer()):
		anotherIndex = cols	
		for k in range(cols):
			B[k][0] = float(matrix[anotherIndex])
			anotherIndex+=(cols+1)
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
	if '' in array:
		array.remove('')
	if "" in array:
		array.remove("")	
	for i in range(len(array)):
		array[i] = (array[i])
	(a,b) = separateMatrices(array)	
	# print(type(b[0][0]),"!!!!!!!!!!!!!!")		
	return (a,b)