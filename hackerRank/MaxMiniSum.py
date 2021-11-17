import math
import os
import random
import re
import sys

arr =[1, 2, 3, 4, 5]

def miniMaxSum(arr):
    arr.sort()
    s = sum(arr)
    maxResult = s - arr[0]
    minResult = s - arr[len(arr) - 1]
    
    print(minResult, maxResult)


def Main():

    miniMaxSum(arr)

print(miniMaxSum(arr))