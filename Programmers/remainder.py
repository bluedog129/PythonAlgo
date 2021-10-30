n = 10

def solution(n):
    x = 1

    while x < n:
        if n % x == 1:
            break
        x += 1
         
    return x

print(solution(n))


def solution(n):
    for i in range(2,n):
        if(n%i==1):
            return i

print(solution(n))