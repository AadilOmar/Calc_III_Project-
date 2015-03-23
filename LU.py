from matrix_multiply import mult
from numpy import *
#from sympy import Eq, Symbol, solve


def getDeterminant():
	print("working on it")
	
def findMaxEigenValue():
	print("working on it")
	#if(triangularMatrix):
		#diagonal elements
	#else:

def computeError(matrix):
	maxEigen = findMaxEigenValue();

def getArrayToFindNorm(l,u,b):
	#return (mult(l,u)-b)
	print("working on it")

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
total = getArrayToFindNorm(l,u,b)	
computeError(total)


