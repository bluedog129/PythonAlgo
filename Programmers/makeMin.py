A = [1, 4, 2]
B = [5, 4, 4]

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i]*B[i]


    return answer

print(solution(A,B))