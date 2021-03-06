n = int(input())
t = []
p = []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
# 받은 돈을 넣은 리스트
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    # 정해진 날짜(7) < i날짜 + 걸리는 시간
    if n < t[i] + i:
        # 퇴사일을 넘기는 일정은 더하지 않는다
        dp[i] = dp[i + 1]
    else:
        # i날짜에 상담을 하는 것과 안 하는 것 중 큰 것을 선택
        dp[i] = max(dp[i + 1], p[i] + dp[t[i] + i])

print(dp[0])