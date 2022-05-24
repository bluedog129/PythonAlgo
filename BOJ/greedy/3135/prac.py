c, w = map(int, input().split())
saved_list_n = int(input())

saved_list = []

[saved_list.append(int(input())) for _ in range(saved_list_n)]

min_value = 1001
optimal = 0

for i in saved_list:
    if min_value > abs(i - w):
        min_value = abs(i - w)
        optimal_saved = i

print(min(abs(c - w), abs(optimal_saved - w) + 1))