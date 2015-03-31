import numpy as np
from convolution import *
import fileinput
import sys


def getArgument():
	toDo = ""
	if(sys.argv[1].isdigit()):
		toDo = "encode"
	else:
		toDo = "iterative"	
	return (toDo,sys.argv[1])
	

def readJacobiFile():
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
	(A,Y) = readJacobiFile()
	startingValue = list(input("enter initial guess in this format: [1,2,3] "))
	start = [[0 for x in range(1)] for x in range(len(A))]
	for i in range(len(A)):
		start[i][0] = startingValue[i]
	error = input("enter error ")
	return (A,Y,start,error)

def printEncodedOutput(yCode, decodedStream,iterations):
	f = open('output.txt','w')
	if(iterations<=0):
		iterations = "Method does not converge after 100 iterations"
	f.write ("Jacobi Method Encoding/Decoding Problem:\n")
	f.write ("y stream output: \n%s\n"%np.matrix(yCode))
	f.write ("decoded stream: \n%s\n"%np.array(decodedStream))
	f.write ("Iterations: %s\n"%iterations)
	f.write("\n")
	f.close()

def printIterative(answer,iterations):
	print iterations
	if(iterations<=0):
		iterations = "Method does not converge after 100 iterations"
	f = open('output.txt','w')
	f.write ("Jacobi Method Iterative Method:\n")
	f.write ("Iterations needed: %s\n"%iterations)
	f.write("\n")
	f.close()


(status,argument) = getArgument()
if(status=="encode"):
	(y0,y1,yCode,A0,A1,codeList) = encodingProblem(int(argument))
	(iterations,answer) = decodingJacobi(A0,A1,y0,y1)
	# print np.array(answer)
	printEncodedOutput(yCode,answer,iterations)


else: #status is iterative
	(A,Y,startingValue,error) = getInput()
	(jacobiIterations,answer) = jacobi(A,Y,startingValue,float(error))
	print jacobiIterations,"================="
	printIterative(answer,jacobiIterations)