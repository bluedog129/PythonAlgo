people_n = int(input())

people_list = []

for _ in range(people_n):
    w, h = map(int, input().split())
    people_list.append((w, h))

for i in people_list:
    rank = 1
    for j in people_list:
        if (i[0] < j[0]) & (i[1] < j[1]):
            rank += 1

    print(rank)