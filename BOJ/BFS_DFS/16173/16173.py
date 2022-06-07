import sys
sys.setrecursionlimit(10**9)

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

visited = []
for _ in range(n):
    visited.append([False] * n)

dx = [1, 0]
dy = [0, 1]

def dfs(x, y, visited):
    if x >= n or x <= -1 or y >= n or y <= -1:
        return 0
    if visited[x][y] == True:
        return 0
    if array[x][y] == -1:
        print('HaruHaru')
        exit()
    visited[x][y] = True
    for i in range(2):
        nx = x + dx[i] * array[x][y]
        ny = y + dy[i] * array[x][y]
        dfs(nx, ny, visited)
    return True

if dfs(0, 0, visited) == True:
    print('Hing')