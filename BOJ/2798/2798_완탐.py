n, m = map(int, input().split())
n_list = list(map(int, input().split()))

n_len = len(n_list)
sum = 0

for i in range(0, n_len - 2):
    for j in range(i + 1, n_len - 1):
        for k in range(j + 1, n_len):
            if (n_list[i] + n_list[j] + n_list[k]) > m:
                continue
            else:
                sum = max(sum, n_list[i] + n_list[j] + n_list[k])

print(sum)