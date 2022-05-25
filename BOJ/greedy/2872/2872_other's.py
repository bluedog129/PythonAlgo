n = int(input())

book_list = []

for _ in range(n):
    book_list.append(int(input()))

find_target = n
answer = 0

for i in range(n - 1, -1, -1):
    if book_list[i] != find_target:
        answer += 1
    else:
        find_target -= 1

print(answer)