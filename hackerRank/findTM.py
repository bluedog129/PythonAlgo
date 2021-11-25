arr = [5,3,1,2,4]

def findMedian(arr):
    arr.sort()
    
    return arr[int(len(arr)/2)]

print(findMedian(arr))