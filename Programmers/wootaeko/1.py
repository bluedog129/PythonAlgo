arr = [2, 1, 3, 1, 2, 1]

def solution(arr):
    # answer.append(arr.count(2))
    answer = []
    count_list = []
    

    for x in arr:
        count_list.append(arr.count(x))

        

    return answer

print(solution(arr))