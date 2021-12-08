land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

#1
# 이전과 같은 열의 값을 제외한 다음 행의 최댓값을 더하는 문제
# 해당 코드는 i행에서 최대값을 가지는 인덱스값이 2개 이상 있을때 논리적오류가 생긴다.
# def solution(land):
#     answer = 0
#     Max = 0
    
#     for i in range(len(land)):
#         Max = max(land[i])
#         answer += Max
#         for j in range(len(land[i])):
#             if Max == land[i][j] and i < len(land)-1:
#                 land[i+1][j] = -1

#     return answer

# print(solution(land))


def solution(land):

    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[len(land)-1])

print(solution(land))