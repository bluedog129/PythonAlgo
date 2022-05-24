n = int(input())
c_list = []
discount = 0

for _ in range(n):
    c_list.append(int(input()))

c_list.sort(reverse = True)

for i in range(n):
    if i % 3 == 2:
        discount += c_list[i]

print(sum(c_list) - discount)