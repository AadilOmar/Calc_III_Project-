# Calc_III_Project-


PART 1: The Hilbert Matrix

	Solve Hilbert:
		Solve with LU:
			run program with filename "solve_lu_b.py" with no parameters
		Solve with QR-householders:
			run program with filename "QR.py" with one parameter: "h"
		Solve with QR-givens:
			run program with filename "QR.py" with one parameter: "g"			


	Running LU/QR:
		Run LU:
			run program with filename "solve_lu_b.py" with a fileName parameter eg:("nameOfFile.dat")
		Run QR-Householders:
			run program with filename "QR.py" with 2 parameters:
				fileName parameter eg:("nameOfFile.dat") and "h"
		Run QR-Givens:
			run program with filename "QR.py" with 2 parameters:
				fileName parameter eg:("nameOfFile.dat") and "g"		

	Solving a Matrix:
		Solve with LU:
			run program with filename "solve_lu_b.py" with 2 params: 
				fileName parameter eg:("nameOfFile.dat") and "solve"
		Solve with QR-Householders:
			run program with filename "QR.py" with 3 params:
				fileName parameter eg:("nameOfFile.dat"), "h", and "solve"


PART 2: Convolution Codes:

	To run encoding/decoding problem:
		Run either jacobi.py or gauss_seidel.py with the argument n(length of stream). 
		This will run the encoding and the decoding of the stream and wil print output to output.txt
		ex: "jacobi.py  6"

	To run Iterative Method:
		Run either jacobi.py or gauss_seidel.py with the argument f(file containing an augmented matrix)
		The user will be asked to input through command-line the initial guess vector ([x1,x2,x3..etc])
		The user will then be asked to input through command-line the tolerance to use
		The	output will be printed to output.txt
		ex: "gauss_seidel.py  matrix.dat"

Part 3: 		