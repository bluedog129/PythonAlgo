arr = [4,3,2,1]

def solution(arr):
    answer = []
    Min = min(arr)

    for i in range(len(arr)):
        
        if arr[i] > Min:
            answer.append(arr[i])

    if len(answer) <= 1:
        return [-1]

    return answer

print(solution(arr))