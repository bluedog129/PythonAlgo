import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
list_n = []

def dfs():
    if len(list_n) == m:
        print(' '.join(map(str, list_n)))

    for i in range(1, n + 1):
        list_n.append(i)
        dfs()
        list_n.pop()

dfs()