import math
import os
import random
import re
import sys

arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    N=len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for number in arr:
        if(number > 0):
            positive_count += 1
        elif(number == 0):
            zero_count += 1
        elif(number < 0):
            negative_count += 1
    
    print("{0:.6f}".format(positive_count/N))
    print("{0:.6f}".format(negative_count/N))
    print("{0:.6f}".format(zero_count/N))

print(plusMinus(arr))