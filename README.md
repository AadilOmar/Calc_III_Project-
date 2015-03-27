# Calc_III_Project-


PART 1:
	Calculating LU:
		Run the program with filename "solve_lu_b.py" with either 0 or 1 more argument
		If no other argument is given, automatically do hilbert and print output to output.txt file
		If argument (file containing matrix) is given, LU is done on the matrix and printed to output.txt file
		If the matrix given is not augmented, it is automatically augmented with [1] matrix to find a solution
		ex: "solve_lu_b.py"
		ex: "solve_lu_b.py  matrix.dat"


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