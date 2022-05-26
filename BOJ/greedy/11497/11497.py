t = int(input())

for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()
    result = 0

    for i in range(2, n):
        result = max(result, abs(n_list[i] - n_list[i - 2]))
    print(result)