t = int(input())

for _ in range(t):
    n = int(input())

    cnt0_list = [1, 0]
    cnt1_list = [0, 1]

    if n > 1:
        for i in range(n - 1):
            cnt0_list.append(cnt1_list[-1])
            cnt1_list.append(cnt0_list[-2] + cnt1_list[-1])

    print(cnt0_list[n], cnt1_list[n])