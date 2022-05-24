n, l = map(int, input().split())
h = list(map(int, input().split()))

temp = 0

# 길이가 가장 작은 과일부터 '스버'에게 먹여야한다 (정렬)
for i in range(len(h) - 1, 0, -1):
    for j in range(i):
        if h[j] > h[j + 1]:
            temp = h[j]
            h[j] = h[j + 1]
            h[j + 1] = temp

for i in h:
    if i <= l:
        l += 1

print(l)