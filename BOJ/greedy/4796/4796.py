n = 1

while True:
    L, P, V = map(int, input().split())
    result = 0

    if L + P + V == 0:
        break

    result += (V // P) * L
    result += min((V % P), L)

    print('Case %d: %d' %(n, result))
    n += 1

