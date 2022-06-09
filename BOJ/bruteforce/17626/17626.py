n = int(input())

minCount = 4

def bf(n, count):
    global minCount

    if n == 0:
        minCount = min(minCount, count)
        return
    if count > minCount:
        return

    for i in range(int(n ** 0.5), int((n // (4 - count)) ** 0.5), -1):
        bf(n - i ** 2, count + 1)

bf(n, 0)
print(minCount)