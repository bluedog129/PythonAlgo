left = 13
right = 17

def count_measure(number):
    count = 0
    for j in range(1, number):
        if number % j == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = count_measure(i)

        if count % 2:
            answer += i
        else : 
            answer -= i

    return answer

print(solution(left, right))