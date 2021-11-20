arr = [1,1,3,2,1]

def countingSort(arr):
    # 이전 코드
    # countArr = list(0 for i in range(len(arr)))
    #####################################################
    
    # 변경 코드
    # arr배열 크기의 조건은 10의 6제곱 까지이나
    # '0 <= arr[i] < 100'의 조건을 만족시키기 위해 다음 코드로 변경 
    countArr = list(0 for i in range(100))

    # counting sort
    for num in arr:
        countArr[num] += 1

    return countArr

print(countingSort(arr))