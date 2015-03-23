

def mult(arr1,arr2):
	rows1 = len(arr1)
	cols1 = len(arr1[0])
	rows2 = len(arr2)
	cols2 = len(arr2[0])
	if(cols1!=rows2):
		print("matrices cannot be multuplied. Wrong sizes");
		return;
	product = [[0 for x in range(cols2)] for x in range(rows1)]
	
	for x in range(rows1): #for each item in the row of arr1
		for y in range(cols2): #for each item in the cols of arr2
			for z in range(rows2): 
			  product [x][y] += arr1[x][z]*arr2[z][y]
	return product

