arr = [2,6,8,14]


def solution(arr):
    from math import gcd
    answer = arr[0]

    for num in arr:
        answer = answer*num // gcd(answer, num)
    
    return answer
        

print(solution(arr))