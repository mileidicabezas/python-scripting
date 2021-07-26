#!/usr/bin/env python3

def get_decimal_from_binary():

	binary_number = [1,0,1,1,0,1,1,0]

	deciaml_number = 0
	counter = 0

	binary_formula = [128, 64, 32,16, 8, 4, 2, 1]
	while counter < len(binary_formula):
		if binary_number[counter]==1:
			deciaml_number += binary_formula[counter]
			print(binary_formula[counter])
		else:
			binary_number[counter] = 0
		counter = counter +1 
	print('The deciaml number is:')
	print(deciaml_number)
		

	



get_decimal_from_binary()




