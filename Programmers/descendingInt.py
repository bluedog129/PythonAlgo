n = 118372

def solution(n):
    answer = 0
    
    n = list(str(n))
    n.sort(reverse=True)
    answer = int(''.join(n))

    return answer

print(solution(n))