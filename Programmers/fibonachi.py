n = 7

def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return (solution(n-1) + solution(n-2)) % 1234567

print(solution(n))

def fib(n):
    if n < 2:
        return n
    
    a, b = 0, 1

    for i in range(n-1):
        a, b = b, a+b
    
    return b

print(fib(n))

def sol(n):
    answer = [0,1]
    for i in range(2,n+1):
        answer.append((answer[i-1] + answer[i-2]))
    
    return answer[n] % 1234567

print(sol(n))