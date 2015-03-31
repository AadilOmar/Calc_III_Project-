from matrix_multiply import *
import numpy as np;
import fileinput
import sys

# matrix1 = [[1,2,0],[-2,1,2],[1,3,1]]

leslie = [
[0,1.2,1.1,0.9,0.1,0,0,0,0],
[0.7,0,0,0,0,0,0,0,0],
[0,0.85,0,0,0,0,0,0,0],
[0,0,0.9,0,0,0,0,0,0],
[0,0,0,0.9,0,0,0,0,0],
[0,0,0,0,0.88,0,0,0,0],
[0,0,0,0,0,0.8,0,0,0],
[0,0,0,0,0,0,0.77,0,0],
[0,0,0,0,0,0,0,0.4,0]]

leslieMod = [
[0,1.2,1.1,0.9,0.1,0,0,0,0],
[0.7,0,0,0,0,0,0,0,0],
[0,0.425,0,0,0,0,0,0,0],
[0,0,0.9,0,0,0,0,0,0],
[0,0,0,0.9,0,0,0,0,0],
[0,0,0,0,0.88,0,0,0,0],
[0,0,0,0,0,0.8,0,0,0],
[0,0,0,0,0,0,0.77,0,0],
[0,0,0,0,0,0,0,0.4,0]]


output = open("output.txt", "w")

def Power(matrix, tol, guess):
    eigenVector = mMult(matrix, guess);
    eigenVectorTest = mMult(matrix, guess);
    eigenVectorTest = mMult(matrix, eigenVectorTest)
    j = 0
    while j < 100:
        eigenVector = mMult(matrix, eigenVector)
        for i in range (0, len(eigenVector)):
            if(eigenVector[len(eigenVector)-1][0]!=0):
                eigenVector[i][0] /= eigenVector[len(eigenVector)-1][0]
            

        eigenVectorTest = mMult(matrix, eigenVectorTest)
        for i in range (0, len(eigenVectorTest)):
            if(eigenVectorTest[len(eigenVectorTest)-1][0]!=0):
                eigenVectorTest[i][0] /= eigenVectorTest[len(eigenVectorTest)-1][0]

        #Initialize numerators and denomenators for Rayleigh quotient
        eigenNum = 0
        eigenDenom = 0
        eigenTestNum = 0
        eigenTestDenom = 0
        eigenValue = 0
        eigenValueTest = 0
        #Calculate Eigenvalue
        for i in range (0, len(eigenVector)):
            eigenNum += mMult(matrix, eigenVector)[i][0] * eigenVector[i][0]
            eigenDenom += eigenVector[i][0] * eigenVector[i][0]
        if(eigenDenom!=0):    
            eigenValue = eigenNum / eigenDenom

        #Calculate Eigenvalue after one more iteration
        for i in range (0, len(eigenVectorTest)):
            eigenTestNum += mMult(matrix, eigenVectorTest)[i][0] * eigenVectorTest[i][0]
            eigenTestDenom += eigenVectorTest[i][0] * eigenVectorTest[i][0]
        if(eigenTestDenom!=0):
            eigenValueTest = eigenTestNum / eigenTestDenom
        error = abs(eigenValueTest - eigenValue)

        j += 1

        if error <= tol:
            output.write("Largest eigenvalue: " + str(eigenValue))
            output.write ("\nThe corresponding eigenvector is: \n%s"%np.matrix(eigenVector))
            output.write("\nThe eigenvalue was found in " + str(j) + " iterations.")
            j = 100 
    if error > tol:
        output.write("The method didn't return a result in 100 iterations.")

    output.close()

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

def readPowerFile():
    total = "" 
    for line in fileinput.input():
        total+=line
    total = total.replace('\n',' ') 
    array = total.split(' ')
    for i in range(len(array)):
        array[i] = (array[i])
    (a,b) = separateMatrices(array) 
    return (a,b)


def getInput():
    (A,Y) = readPowerFile()
    startingValue = list(input("enter initial guess in this format: [1,2,3] "))
    start = [[0 for x in range(1)] for x in range(len(A))]
    for i in range(len(A)):
        start[i][0] = startingValue[i]
    error = input("enter error ")
    return (A,Y,start,error)

def getActualLeslie(n):
    actual = [[0 for x in range(n)] for x in range(n)]
    for i in range(x):
        for j in range(x):
            actual[i][j] = leslie[i][j]
    return actual

(A,Y,start,error) = getInput()
matrix = getActualLeslie(len(A))
Power(A, error, start)
