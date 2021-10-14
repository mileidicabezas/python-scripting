#!/usr/bin/env python3

# permisopns to run the script: chmod u+x multiples_of_a_number.py
# run script: ./multiples_of_a_number.py

''' 
Task:
Write a script that prints the multiples of 7 between 0 and 100. 
Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
Remember that 0 is also a multiple of 7.
'''

def multiples_of_a_number():
    for x in range(0,100):
        if x % 7 == 0 and x < 100:
            print(x)

multiples_of_a_number()




