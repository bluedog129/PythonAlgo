t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    a_mod = a % 10

    # 패턴별로 다 나누어 주어야 한다
    # 1 pattern : (a ** b) % 10 의 값이 1개의 경우로 정해져 있을 때
    if a_mod == 0:
        print(10)
    elif a_mod in [1, 5, 6]:
        print(a_mod)
    # 2 pattern
    elif a_mod in [4, 9]:
        b_mod = b % 2
        if b_mod == 0:
            print(a_mod * a_mod % 10)
        else:
            print(a_mod)
    # 4 pattern
    elif a_mod in [2, 3, 7, 8]:
        a_mod = a % 4
        if b_mod == 0:
            print(a_mod ** 4 % 10)
        else:
            print(a_mod ** b_mod % 10)