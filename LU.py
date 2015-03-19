from matrix import mult;


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

 
b =	[[2,4,-4],
	[1,-4,3],
	[-6,-9,5]];
computeLU(b);


