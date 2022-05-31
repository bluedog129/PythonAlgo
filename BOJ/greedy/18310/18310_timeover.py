n = int(input())
min_sum = 100000
dis_sum = 0
result = 0

house_list = list(map(int, input().split()))

for i in range(len(house_list)):
    for house in house_list:
        dis_sum += abs(house_list[i] - house)

    if min_sum > dis_sum:
        min_sum = dis_sum
        result = house_list[i]

print(result)