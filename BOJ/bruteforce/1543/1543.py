origin_str = input()
find_str = input()
count = 0
index = 0

for i in range(len(origin_str)):
    if i < index:
        continue

    if find_str == origin_str[i: i + len(find_str)]:
        count += 1
        index = i + len(find_str)

print(count)