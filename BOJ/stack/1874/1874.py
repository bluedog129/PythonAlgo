n = int(input())
n_list = []
stack = []
result = []
count = 1
ok = True

for _ in range(n):
    n_list.append(int(input()))

for num in n_list:
    while num >= count:
        stack.append(count)
        result.append('+')
        count += 1

    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        ok = False
        break

if ok == False:
    print("NO")
else:n = int(input())
n_list = []
stack = []
result = []
count = 1
ok = True

for _ in range(n):
    n_list.append(int(input()))

for num in n_list:
    while num >= count:
        stack.append(count)
        result.append('+')
        count += 1

    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        ok = False
        break

if ok == False:
    print("NO")
else:
    for i in result:
        print(i)

    for i in result:
        print(i)