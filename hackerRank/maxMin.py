import sys

arr = [1,4,7,2]
k = 2

# 배열을 정렬한 후에 각 배열간의 차이를 구한 배열을 만들고, 
# Queue처럼 한칸씩 움직이며 Min값을 체크하는 식으로 구현하였다.

def maxMin(k, arr):
    arr.sort()
    diff = []
    unfairness = 0
    min = sys.maxsize

    # 각 리스트인덱스간의 값 차이를 diff리스트에 넣어준다.
    for i in range(len(arr)-1):
        diff.append(arr[i+1] - arr[i])

    # diff리스트의 값들을 unfairness에 더해준다.
    for i in range(k - 1):
        unfairness += diff[i]
    
    # unfairness 값을 min에 넣어줌
    min = unfairness

    # diffdml 
    for i in range(k-1, len(diff)):
        unfairness -= diff[i-(k-1)]
        unfairness += diff[i]

        if min > unfairness:
            min = unfairness
    
    return min

print(maxMin(k, arr))