x = 10

def solution(x):
    arr = list(str(x))
    sum = 0

    for i in range(len(arr)):
        sum += int(arr[i])
        if x % sum == 0:
            answer = True
        else:
            answer = False

    return answer

print(solution(x))

def solution(x):
    sum = 0
    num = x
    while x > 0:
        sum += x%10
        x = int(x/10)
        
    if num % sum == 0:
        return True
    else:
        return False

print(solution(x))