n = int(input())

book_list = []

for _ in range(n):
    book_list.append(int(input()))

last_book = n
last_book_idx = book_list.index(last_book)
minus = 0

for i in range(last_book_idx, -1, -1):
    if book_list[last_book_idx] - 1 == book_list[i]:
        minus += 1
        last_book_idx = i

print(n - minus - 1)