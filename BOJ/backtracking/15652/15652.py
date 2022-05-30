n, m = map(int, input().split())
n_list = []

def bfs(start):
    if len(n_list) == m:
        print(' '.join(map(str, n_list)))
        return

    for i in range(start, n + 1):
        n_list.append(i)
        bfs(i)
        n_list.pop()

bfs(1)