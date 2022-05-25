t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    aa = a % 10

    # 부르트포스로 하면 안 되기에
    # 각 패턴으로 나누어 최대한 연산을 줄여준다
    # 패턴 1개
    if aa == 0:
        print(10)
    elif aa in [1, 5, 6]:
        print(aa)
    # 패턴 2개
    elif aa in [4, 9]:
        bb = b % 2
        if bb == 0:
            print(aa * aa % 10)
        else:
            print(aa)
    # 패턴 4개
    else:
        bb = b % 4
        if bb == 0:
            print(aa ** 4 % 10)
        else:
            print(aa ** bb % 10)
