arr = [1,2,3,4]

def solution(arr):
    answer = 0
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]
    
    answer = sum/len(arr)

    return answer

print(solution(arr))