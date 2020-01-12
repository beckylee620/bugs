#! /usr/local/bin/python3

## ./generate_bugs.py width length

import sys
import math
import numpy as np
import itertools

width = int(sys.argv[1])
half_width = math.ceil(width/2)
length = int(sys.argv[2])
unique_pixels = half_width * length

# count up in binary to find every combination of 0+1
# in a symmetrical matrix of the given dimensions
for i in itertools.product([0,1],repeat=unique_pixels):
# make an array
    matrix = np.reshape(np.array(i),(length,half_width))
    valid,bug = True,False
    while valid:
# check that every row and every column have a 1
        for x in range(0,half_width):
            if not 1 in matrix[:,x]:
                valid = False
        for y in range(0,length):
            if not 1 in matrix[y,:]:
                valid = False
# check that there are no free-floating 1s
# and that there is exactly one eye
        eyes = 0
        for x in range(0,half_width-2):
            for y in range(0,length-2):
                if np.array_equal(matrix[y:y+3,x:x+3],np.array([[1,1,1],[1,0,1],[1,1,1]])):
                    eyes += 1
                if np.array_equal(matrix[y:y+3,x:x+3],np.array([[0,0,0],[0,1,0],[0,0,0]])):
                    valid = False
#!! look along edges and middle for lonely 1s
#!! and look along middle for extra eyes
        if eyes != 1:
            valid = False
        if valid:
            bug = True
            valid = False
# when a valid bug is found:
#!! print matrix number by converting to binary
#!! print nicely-formatted reflected matrix (accounting for even numbers of columns)
    if bug:
        print(matrix)
