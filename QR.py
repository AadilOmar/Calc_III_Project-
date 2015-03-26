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

def Qr_fact_househ(matrix):

        R = np.copy(matrix)
        matrixARows, matrixACols = np.shape(matrix)

        #Construct an nxn identity matrix
        Q = np.identity(matrixARows)

        for i in range(matrixARows-1):
            x = R[i:, i]
            e = np.zeros_like(x)
            e[0] = copysign(np.linalg.norm(x), -A[i,i])
            u = x + e
            v = u / np.linalg.norm(u)
            Q_2 = np.identity(matrixARows)
            Q_2[i:, i:] -= 2.0 * np.outer(v,v)

            #Multiply, or "Dot Product" out R with Q_2
            R = np.dot(Q_2, R)
            #Multiply/Dot Product out Q with Q_2
            Q = np.dot(Q, Q_2.T)

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

        

def DoEverythingQRHouseholders(A):
        Q, R = Qr_fact_househ(A)
        return (Q,R)
#	y = findY(l,b)
#	x = findX(u,y)
#	arr = getArrayToFindNorm(l,u,A)
#	e = computeError(arr)
#	return (l,u,y,x,e)
#
