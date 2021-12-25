n = 15

def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
    
    return answer

print(solution(n))

def solution(n):
    # n이하인 숫자 a부터 k개의 연속된 숫자의 합이 n이라고 가정한다면
    return len([i  for i in range(1,n+1,2) if n % i is 0])

print(solution(n))