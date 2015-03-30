from matrix_multiply import *
from LU import rowReduce
from LU import convertToUpperTriangle
from LU import flipMatrix
from LU import findX
from LU import getArrayToFindNorm
import numpy as np
import scipy
import scipy.linalg
import pprint
from math import sqrt
from math import *

output = open("output.txt", "w")

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

def normOfVector(x):
        sumOfNumbersSquared = sum([i**2 for i in x])
        total = sqrt(sumOfNumbersSquared)
        return total
    
def Qr_fact_househ(matrix):
        matrix = np.asarray(matrix)
        #Clone matrix A into matrix R
        R = np.copy(matrix)

        #Get the respective rows and column length of matrix A
        matrixARows, matrixACols = np.shape(matrix)

        #Construct an nxn identity matrix
        Q = np.identity(matrixARows)

        for i in range(matrixARows-1):
            x = R[i:, i]
            e = np.zeros_like(x)
            #e[0] = copysign(np.linalg.norm(x), -A[i,i])
            e[0] = copysign(normOfVector(x), -matrix[i,i])
            u = x + e
            
            #Successfully used my method defined above to find norm
            #instead of numpy's method
            u_norm = normOfVector(u)
            v = u / u_norm
            Q_2 = np.identity(matrixARows)
            outerMatrix = np.outer(v,v)
            Q_2[i:, i:] -= 2.0 * outerMatrix
            
            #Multiply, or "Dot Product" out R with Q_2
            #Trying Aadil's method-which returns a list, which I then convert to a numpy array
            R = np.asarray(mMult(Q_2, R))
            #Multiply/Dot Product out Q with Q_2
            #Try it with Aadil's method and cast it into a numpy array from a list
            Q = np.asarray(mMult(Q, Q_2.T))

 
        #Get's rid of the values in R that shouldn't be there for it to be an upper triangular matrix
        R = np.triu(R)
        
        #Fix up discrepencies in Q -- Actually, may not be necessary
        #Q = -1 * Q
    
        #Fix up discrepencies in R -- Actually, may not be necessary
        #R = -1 * R

        return Q, R
        
def qr_fact_givens(matrix):

    n = len(matrix) - 1

    #Create a matrix to be turned into the identity matrix
    baseMatrix = [row[:] for row in matrix]

    #Create a matrix to be turned into the Givens matrix
    newMatrix = [row[:] for row in matrix]

    #Create a matrix that remains a copy of the provided matrix
    ogMatrix = [row[:] for row in matrix]

    #Create a matrix that becomes the R in the QR factorization
    r = [row[:] for row in matrix]

    #Sets baseMatrix to the identity matrix
    for i in range(0, n+1):
        for j in range(0, n+1):
            if i == j:
                baseMatrix[i][j] = 1
            else:
                baseMatrix[i][j] = 0

    #Main rotation matrix
    for i in range (0, n):
        for j in range(i, n):
            x1 = r[i][i]
            x2 = r[j+1][i]

            #Sets newMatrix back to the identity each iteration
            newMatrix = [row[:] for row in baseMatrix]

            cosThet = (x1) / math.sqrt(x1 * x1 + x2 * x2)
            sinThet = -(x2) / math.sqrt(x1 * x1 + x2 * x2)

            #Sets newMatrix to the Givens matrix for the current iteration
            newMatrix[i][i] = cosThet
            newMatrix[i][j+1] = -1 * sinThet
            newMatrix[j+1][i] = sinThet
            newMatrix[j+1][j+1] = cosThet

            #If it is the first iteration, initializes q
            if i == 0 and j == 0:
                q = [row[:] for row in newMatrix]
                q[i][j+1] *= -1
                q[j+1][i] *= -1
            #Otherwise, multiplies q by the transpose of the current G matrix
            else:
                qTemp = [row[:] for row in newMatrix]
                qTemp[i][j+1] *= -1
                qTemp[j+1][i] *= -1
                q = mult(q, qTemp)

            r = mult(newMatrix, r)

    qrMatrix = mult(q, r)
    error = [row[:] for row in qrMatrix]
    for i in range(0, n+1):
        for j in range(0, n+1):
            error[i][j] = qrMatrix[i][j] - matrix[i][j]

    print(q)
    print(r)
    print(computeError(error))

    #Prints Q to the output file
    firstLine = str(q[0])
    output.write("Q = " + firstLine + "\n")
    for i in range(1, n+1):
        newLine = str(q[i])
        output.write("    " + newLine + "\n")

    output.write("\n\n")

    #Prints R to the output file
    firstLine = str(q[0])
    output.write("R = " + firstLine + "\n")
    for i in range(1, n+1):
        newLine = str(r[i])
        output.write("    " + newLine + "\n")

    output.write("\n\n")

    #Prints the error to the output file
    errorString = str(computeError(error))
    output.write("||A-QR||max = " + errorString)

    output.close()

def solve_qr_b(Q, R, b):
    y = mMult(Q.transpose(), b)
    y = np.asarray(y) #Conveting to a numpy assoc array for consistency with other matrices
    x = findX(R, y) #Coverting to a numpy assoc array for consistency with other matrices
    return y, x



def DoEverythingQRHouseholders(A, b):
    Q, R = Qr_fact_househ(A) #Works
    y, x = solve_qr_b(Q, R, b)
    QR = mMult(Q, R)
    e = computeError(np.subtract(QR, A))
    return Q, R, y, x, e
    
    
#        return (Q,R)
#	y = findY(l,b)
#	x = findX(u,y)
#	arr = getArrayToFindNorm(l,u,A)
#	e = computeError(arr)
#	return (l,u,y,x,e)
#

#Constructing a matrix A for testing purposes
#A = np.matrix([[12,-51,4], [6,167,-68], [-4,24,-41]])


#Does everything
A = ([[1, 0.5, 0.333333, 0.25],[0.5, 0.333333, 0.25, 0.2], [0.333333, 0.25, 0.2, 0.166667], [0.25, 0.2, 0.166667, 0.142857]])
b = np.asarray([[0.0464159],[0.0464159],[0.0464159],[0.0464159]])
#Q, R = Qr_fact_househ(A)
#x = solve_qr_b(A, b)
