# 1 부터 n 까지 자연수 중에서 중복 없이 m개를 고른 수열 즉, 길이가 m인 수열
n, m = map(int, input().split())
num_list = []

def dfs():
    # 정해진 길이(m)을 만족하면 출력
    if len(num_list) == m:
        print(' '.join(map(str, num_list)))
        return

    # 1 ~ n 만큼 반복
    for i in range(1, n + 1):
        # num_list에 중복되는 값이 없어야 함
        if i not in num_list:
            # 중복되지 않는 값을 num_list에 넣음
            num_list.append(i)
            # num_list의 길이가 m에 도달하지 않았다면 다시 재귀로 들어감
            dfs()
            # 출력 후에 재귀가 끝나고 다시 num_list에 다른 i값을 넣기 위해 pop()
            num_list.pop()

dfs()