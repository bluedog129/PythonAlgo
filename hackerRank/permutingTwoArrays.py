k = 10
A = [7,6,8,4,2]
B = [5,2,6,3,1]

def twoArrays(k, A, B):
    count = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(0, len(A)):
        if A[i] + B[i] >= k:
            count += 1
        
        if count == len(A):
            return "YES"
    return "NO"

print(twoArrays(k, A, B))