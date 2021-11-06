n = 3
m = 12

def gcd(n, m):
    mod = m%n
    if mod != 0:
        m, n = n, mod
        return gcd(n,m)
    else:
        return n

def solution(n, m):
    
    return [gcd(n,m),int(m*n/gcd(n,m))]

print(solution(n, m))