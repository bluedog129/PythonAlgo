from collections import deque

t = int(input())

for i in range(t):
    n = int(input())
    l = sorted(map(int, input().split()))
    res = 0

    deq = deque()
    if n % 2 == 1:
        deq.append(l.pop(-1))
    for j in range(n // 2):
        deq.append(l.pop(-1))
        deq.appendleft(l.pop(-1))

    for a in range(n - 1):
        b = a + 1
        if res < abs(deq[a] - deq[b]):
            res = abs(deq[a] - deq[b])

    print(res)