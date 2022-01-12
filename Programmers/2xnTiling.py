n = 4

# 문제를 따라 타일 계산을 하다보면 f(x) = f(x-1) + f(x-2) 인 것을 알기 때문에
# 가로의 길이 1 = f(1) = 1, 가로의 길이 2 = f(2) = 2라 가정하면
# arr[1] = 1, arr[2] = 2
# for i in range(3, n):
#   arr[i] = arr[i - 1] + arr[i - 2]
# 처럼 풀 수 있습니다.

def solution(n):
    a, b = 1,2
    for i in range(2, n):
        a, b = b, (a+b) % 1000000007

    return b

print(solution(n))