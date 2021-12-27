import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    lastAnswer = 0
    arr = [[] for _ in range(n)]
    ans = []
    q = len(queries)

    for q in queries:
        q_typ = q[0]
        x = q[1]
        y = q[2]
        idx = (x^lastAnswer) % n

        if q_typ == 1:
            arr[idx].append(y)
        elif q_typ == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            ans.append(lastAnswer)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

print(dynamicArray(n, queries))