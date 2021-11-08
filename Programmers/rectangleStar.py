a, b = map(int, input().strip().split(' '))

for i in range(len(b)):
    for j in range(len(a)):
        print('*', end='')
    print()