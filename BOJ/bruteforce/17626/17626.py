n = int(input())

minCount = 4

def bf(n, count):
    global minCount

    if n == 0:
        minCount = min(minCount, count)
        return
    if count > minCount:
        return
    # 재귀의 깊이에 따라 n을 나눈뒤 제곱근 한 값까지만 탐
    for i in range(int(n ** 0.5), int((n // (4 - count)) ** 0.5), -1):
        bf(n - i ** 2, count + 1)

bf(n, 0)
print(minCount)