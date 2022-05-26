lows_len, cols_len = map(int, input().split())

original = []
count_list = []

for _ in range(lows_len):
    original.append(input())

# 체스판의 시작점을 잡는다
# a는 행, b는 열에 대하여 원래의 체스 판에서 8*8로 자를 수 있는 범위의 시작점을 가리킴
for a in range(lows_len - 7):
    for b in range(cols_len - 7):
        # 'W'로 시작할 경우 바뀐 체스 판의 갯수를 세는 변수
        w_change = 0
        # 'B'로 시작할 경우 바뀐 체스 판의 갯수를 세는 변수
        b_change = 0
        # a, b 기준으로 8칸씩 체크
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                # i와 j를 더해야 위치를 제대로 잡을 수 있음
                if (i + j) % 2 == 0:
                    # 짝수칸에 B가 오면 W로 바꿔줌 그 반대는 B로 바꿔줌
                    # 그 상황에 맞게 _index 변수에 더해줌
                    if original[i][j] != 'W':
                        w_change += 1
                    if original[i][j] != 'B':
                        b_change += 1
                else:
                    # 홀수칸은 짝수칸과 반대로
                    if original[i][j] != 'B':
                        w_change += 1
                    if original[i][j] != 'W':
                        b_change += 1
        count_list.append(min(w_change, b_change))

print(min(count_list))