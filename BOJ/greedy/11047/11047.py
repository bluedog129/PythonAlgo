n, k = map(int, input().split())

coin_list = []
count = 0

for _ in range(n):
    coin_list.append(int(input()))

for i in range(n - 1, -1, -1):
    if k == 0:
        break
    count += k // coin_list[i]
    k = k % coin_list[i]

print(count)