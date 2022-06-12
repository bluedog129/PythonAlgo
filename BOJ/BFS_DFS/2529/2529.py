k = int(input())
k_list = list(map(str, input().split()))
visited = [False] * 10
min = ""
max = ""

def possible(i, j, sign):
    if sign == '>':
        return i > j
    else:
        return i < j

def dfs(depth, s):
    global min, max

    if depth == k + 1:
        if len(min) == 0:
            min = s
        else:
            max = s
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or possible(s[len(s) - 1], str(i), k_list[depth - 1]):
                visited[i] = True
                dfs(depth + 1, s + str(i))
                visited[i] = False

dfs(0, "")
print(max)
print(min)