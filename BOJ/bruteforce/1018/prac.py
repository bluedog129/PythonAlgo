lows_len, cols_len = map(int, input().split())

original = []
count_list = []

for _ in range(lows_len):
    original.append(input())

for a in range(lows_len - 7):
    for b in range(cols_len - 7):
        w_change = 0
        b_change = 0

        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if original[i][j] != 'W':
                        w_change += 1
                    else:
                        b_change += 1
                else:
                    if original[i][j] != 'B':
                        w_change += 1
                    else:
                        b_change += 1
        count_list.append(min(w_change, b_change))

print(min(count_list))