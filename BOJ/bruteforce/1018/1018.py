lows_len, cols_len = map(int, input().split())

original = []
count = []

for _ in range(lows_len):
    original.append(input())

# 체스판의 시작점을 잡는다
# a는 행, b는 열에 대하여 원래의 체스 판에서 8*8로 자를 수 있는 범위의 시작점을 가리킴
for a in range(lows_len - 7):
    for b in range(cols_len - 7):
        # 'W'로 시작할 경우 바뀐 체스 판의 갯수를 세는 변수
        index1 = 0
        # 'B'로 시작할 경우 바뀐 체스 판의 갯수를 세는 변수
        index2 = 0
        # a, b 기준으로 8칸씩 체크
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))