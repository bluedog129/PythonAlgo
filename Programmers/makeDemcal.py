from itertools import combinations
nums = [1,2,3,4]

def check(a,b,c):
    total = a+ b + c
    for i in range(2, total):
        if total % i == 0: return False
    return True

def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))
    for i in A:
        if check(i[0], i[1], i[2]): answer +=1
    return answer