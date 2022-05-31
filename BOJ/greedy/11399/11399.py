n = int(input())
n_list = sorted(list(map(int, input().split())))

sum = 0
time = 0

for i in range(n):
    time += n_list[i]
    sum += time

print(sum)