from matrix_multiply import mult
from LU import rowReduce
import numpy as np
import scipy
import scipy.linalg
import pprint
from math import sqrt
from math import *

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

def normOfVector(x):
        sumOfNumbers = sum([i**2 for i in x])
        return sqrt(sumOfNumbers)

def computeQR(matrix):
        Q, R = scipy.linalg.qr(matrix)
        print "A: "
        pprint.pprint(matrix)
        print "Q: "
        pprint.pprint(Q)
        print"R: "
        pprint.pprint(R)

def QRHHBITCH(matrix):

        R = np.copy(matrix)
        matrixARows, matrixACols = np.shape(matrix)
        Q = np.identity(matrixARows)

        for cnt in range(matrixARows-1):
            x = R[cnt:, cnt]
            e = np.zeros_like(x)
            e[0] = copysign(np.linalg.norm(x), -A[cnt,cnt])
            u = x + e
            v = u / np.linalg.norm(u)
            Q_cnt = np.identity(matrixARows)
            Q_cnt[cnt:, cnt:] -= 2.0 * np.outer(v,v)
            R = np.dot(Q_cnt, R)
            #Fix up lower triangular R matrix values
            Q = np.dot(Q, Q_cnt.T)

        #Done with For loop, now fix discrepencies in the matrices
        #Forms the basis of the Lower Triangular Matrix in R
        R[1,0] = 0
        R[2,0] = 0
        R[2,1] = 0
        
        #Fix up discrepencies in Q
        Q = -1 * Q
    
        #Fix up discrepencies in R
        R = -1 * R

        return Q, R

        

#def doEverything(A,b):
#	l,u = computeLU(A)
#	y = findY(l,b)
#	x = findX(u,y)
#	arr = getArrayToFindNorm(l,u,A)
#	e = computeError(arr)
#	return (l,u,y,x,e)
#
