d = [2,2,3,3]
budget = 9

def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    for i in range(len(d)):
        sum += d[i]

        if budget >= sum:
            answer += 1
    
    return answer

print(solution(d, budget))

# sol2
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

print(solution(d, budget))