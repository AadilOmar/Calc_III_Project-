import numpy as np
from matrix_multiply import *
from LU import *
import sys
import random

#gets argument passed in (number of bits to encode)
def getN():
	n = int(sys.argv[1])
	return n

#gets a random binary string n bits long
def generateRandomCode(n):
	codeList = [[0 for x in range(1)] for x in range(n)]
	# list = []
	for i in range(n):
		codeList[i][0] = random.randrange(0,2)
		# list.append(random.randrange(0,2))
	print codeList,"THIS IS THE CODE"	
	return codeList

#using formula, finds the y0 encoding from given  x
def findY0(x):
	l = []
	for i in range(len(x)):
		if(i==0):
			l.append(x[i][0])
		elif(i==1):	
			l.append(x[i][0])
		elif(i==2):
			l.append((x[i][0]+x[i-2][0])%2)
		else:
			l.append((x[i][0]+x[i-2][0]+x[i-3][0])%2)
	toRet = [[0 for j in range(1)] for j in range(len(x))]
	for j in range(len(x)):
		toRet[j][0] = l[j]
	return toRet		

#using formula, finds the y1 encoding from given  x
def findY1(x):
	l = []
	for i in range(len(x)):
		if(i==0):
			l.append(x[i][0])
		elif(i==1):	
			l.append((x[i][0]+x[i-1][0])%2)
		elif(i==2):
			l.append((x[i][0]+x[i-1][0])%2)
		else:
			l.append((x[i][0]+x[i-1][0]+x[i-3][0])%2)
	toRet = [[0 for j in range(1)] for j in range(len(x))]
	for j in range(len(x)):
		toRet[j][0] = l[j]
	return toRet

#gets the total y encoding by conbining both y encodings
def getConvolutionCodeWord(y0,y1):
	l = []
	for i in range(len(y1)):
		toAppend = str(y0[i])+str(y1[i]	)
		l.append(toAppend)
	return l	

#finds A0 using algorithm given
def findA0(n):
	a = [[0 for i in range(n)] for i in range(n)]
	for i in range(len(a)):
		if(i==0):
			a[i][i] = 1
		elif(i==1):
			continue
		elif(i==2):
			a[i][i]=1
			a[i][i-2]=1			
		else:
			a[i][i]=1
			a[i][i-2]=1		
			a[i][i-3]=1			
	return a		

#finds A1 using algorithm given
def findA1(n):
	a = [[0 for i in range(n)] for i in range(n)]
	for i in range(len(a)):
		if(i==0):
			a[i][i] = 1
		elif(i==1):
			a[i][i] = 1
			a[i][i-1] = 1
		elif(i==2):
			a[i][i] = 1
			a[i][i-1] = 1			
		else:
			a[i][i]=1
			a[i][i-1]=1		
			a[i][i-3]=1			
	return a		

#splits up matrix A into L,D,U (necessary for jacobi and gauss iterations)
def getLDUMatrices(A):
	L = [[0.0 for x in range(len(A))] for x in range(len(A))]
	D = [[0.0 for x in range(len(A))] for x in range(len(A))]
	U = [[0.0 for x in range(len(A))] for x in range(len(A))]
	for x in range(len(A)):
		D[x][x] = float(A[x][x])
	for i in range(1,len(A)):
		for j in range(0,i):
			L[i][j] = float(A[i][j])
	for i in range(len(A)-1):
		for j in range(i+1,len(A)):
			U[i][j] = float(A[i][j])
	return (L,D,U)
		
#dot product of two values			
def dot(a,b):
	return np.dot(a,b)

#solves gauss_siedel
def solve_gauss_seidel(A, y, x0, tol):
	(l,d,u) = getLDUMatrices(A)
	LD = np.add(l,d)
	negUxkPlusB = np.add(mMult(dot(-1,u),x0),y)
	xkplus1 = findY(LD,negUxkPlusB)
	return xkplus1

#runs 25 iterations of gauss siedel
def gauss_seidel(A, y, x0, tol):
	numIterations = -1
	answer = []	
	for i in range(25):
		oldX0 = x0
		x0 = solve_gauss_seidel(A, y, x0, tol)
		error = computeError(np.subtract(oldX0,x0))
		if (error<tol):
			answer = x0
			numIterations = i
			break
	return (numIterations,answer)

#solves jacobi
def solveJacobi(A, y, x0, tol):
	(l,d,u) = getLDUMatrices(A)
	negLUxkPlusB = np.add(mMult(dot(-1,np.add(l,u)),x0),y)
	#A=D  b=neg(L+U)x+b  solve for x
	xkplus1 = findX(d,negLUxkPlusB)
	return xkplus1

#runs 25 iterations of jacobi
def jacobi(A, y, x0, tol):
	numIterations = -1
	answer = []	
	for i in range(25):
		oldX0 = x0		
		x0 = solveJacobi(A, y, x0, tol)
		error = computeError(np.subtract(oldX0,x0))
		# print error
		if (error<tol):
			answer = x0
			numIterations = i
			break
	return (numIterations,answer)

#does everything necessary for the encoding portion. returns everything
def encodingProblem(n):
	codeList = generateRandomCode(n) #vertical
	# codeList = [1, 0, 1, 1, 0]#, 0]#, 1, 1, 1, 0, 0, 0, 1, 0] #just a tester
	y0 = findY0(codeList)
	y1 = findY1(codeList)
	A0 = findA0(n)
	A1 = findA1(n)
	yCode = getConvolutionCodeWord(y0,y1)
	return (y0,y1,yCode,A0,A1,codeList)

def decodingJacobi(A0,A1,y0,y1):
	x = [[0 for x in range(1)] for x in range(len(A0))]
	(q,w) = jacobi(A1,y1,x,.000000000000000001)	
	# (q1,w1) = jacobi(A1,y1,x,.000000000000000001)
	for i in range(len(w)):
		w[i][0] = np.absolute((w[i][0])%2)
	return (q,w)

def decodingGauss(A0,A1,y0,y1):
	x = [[0 for x in range(1)] for x in range(len(A0))]
	(q,w) = gauss_seidel(A1,y1,x,.000000000000000001)
	# (q1,w1) = gauss_seidel(A1,y1,x,.000000000000000001)
	for i in range(len(w)):
		w[i][0] = np.absolute((w[i][0])%2)
	return (q,w)

#does everything necessary for the iterative methods. Should prob print to file
def iterativeMethods(A, y, x0, tol):
	#A is square  y is vertical vector  x is vertical vector  
	(gaussIterations,ganswer) = gauss_seidel(A,y,x0,float(total))
	(jacobiIterations,janswer) = jacobi(A,y,x0,float(total))
	return (gaussIterations, ganswer,jacobiIterations,janswer)

#does everything necessary for the decoding portion
def decodingProblem(streamY,A0,A1,x0):
	y1 = [[0 for x in range(1)] for x in range(len(A0))]
	y0 = [[0 for x in range(1)] for x in range(len(A0))]
	for i in range(len(A0)):
		y0[i][0] = float(streamY[i][0])
		y1[i][0] = float(streamY[i][1])
	x0 = findX(A0,y0)	
	x1 = findX(A1,y1)	
	return (x0,x1)
