t = int(input())

for _ in range(t):
    # 0과 1일때 갯수를 초기화
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    n = int(input())
    # 0과 1인 경우는 이미 리스트에 있으므로 1보다 클 경우만 진행
    if n > 1:
        # n - 1 이유? : 1일때 까지 초기화가 되어있기 때문
        for i in range(n - 1):
            # 현재 0의 갯수는 이전 1의 갯수를 가져옴
            cnt_0.append(cnt_1[-1])
            # 현재 1의 갯수는 이전 0의 갯수 + 이전 1의 갯수
            cnt_1.append(cnt_0[-2] + cnt_1[-1])

    print(cnt_0[n], cnt_1[n])