# Calc_III_Project-


PART 1:

	Solve Hilbert:
		Solve with LU:
*			run program with filename "solve_lu_b.py" with parameter "n" eg:("solve_lu_b.py  17") 
		Solve with QR-Householders:
			run program with filename "QR.py with parameter "h" and "n" eg:("qr.py  h  8")
		Solve with QR-Givens:
			run program with filename "QR.py" with parameter "g" and "n" eg:("qr.py  g  13")

	Running LU/QR:
		Run LU:
			run program with filename "solve_lu_b.py" with a fileName parameter eg:("nameOfFile.dat")
		Run QR-Householders:
			run program with filename "QR.py" with a fileName parameter eg:("nameOfFile.dat")
		Run QR-Givens:
			run program with filename "QR.py" with a fileName parameter eg:("nameOfFile.dat")

	Solving a Matrix:
		Solve with LU:
			run program with filename "solve_lu_b.py" with 2 params: 
				fileName parameter eg:("nameOfFile.dat") and "solve"
		Solve with QR-Householders:
			run program with filename "QR.py" with 2 params:
				fileName parameter eg:("nameOfFile.dat") and "solve"
		Solve with QR-Givens:
			run program with filename "QR.py" with 2 params
				fileName parameter eg:("nameOfFile.dat") and "solve"



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