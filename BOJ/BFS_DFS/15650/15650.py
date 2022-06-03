n, m = map(int, input().split())
n_list = []

def dfs(start):
    if len(n_list) == m:
        print(' '.join(map(str, n_list)))

    for i in range(start, n + 1):
        if i not in n_list:
            n_list.append(i)
            dfs(i + 1)
            n_list.pop()

dfs(1)