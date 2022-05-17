from itertools import permutations

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

permutationArray = permutations(n_list, 3)
sum = 0

for i in permutationArray:
    if (m + 1 > sum(i)):
        sum = max(sum, sum(i))

print(sum)