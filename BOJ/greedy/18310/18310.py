n = int(input())
house_list = sorted(list(map(int, input().split())))

print(house_list[(n - 1) // 2])