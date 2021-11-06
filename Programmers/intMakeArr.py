n = 12345

def solution(n):
    arr = list(str(n))
    arr.reverse()
    
    return list(map(int, arr))

print(solution(n))