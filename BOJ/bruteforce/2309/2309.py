n_list = [int(input()) for _ in range(9)]


for i in n_list:
    for j in n_list:
        sum_list = sum(n_list)
        if sum_list - i - j == 100 and i != j:
            n_list.remove(i)
            n_list.remove(j)

n_list.sort()

for i in n_list:
    print(i)