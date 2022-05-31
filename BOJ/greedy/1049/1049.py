n, m = map(int, input().split())

minPack = 1001
minOne = 1001
for _ in range(m):
    package, one = map(int, input().split())
    minPack = min(minPack, package)
    minOne = min(minOne, one)

result = 0

if minPack > minOne * 6:
    result += n * minOne
else:
    result += (n // 6) * minPack

    if (n % 6) * minOne > minPack:
        result += minPack
    else:
        result += (n % 6) * minOne

print(result)