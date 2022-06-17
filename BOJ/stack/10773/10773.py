k = int(input())
n_list = []

for i in range(k):
    n = int(input())
    n_list.append(n)

    if n == 0:
        n_list.pop()
        n_list.pop()

print(sum(n_list))