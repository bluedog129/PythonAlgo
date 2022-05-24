# 주파수 c, w 값 받기
c, w = map(int, input().split())
# 즐겨찾기
saved_num_n = int(input())

arr = []
# arr에 saved_num_n 크기만큼 즐겨찾기 채널 번호를 넣는다.
[arr.append(int(input())) for _ in range(saved_num_n)]

min_value = 1001
idx = 0

for i in arr:
    # 즐겨찾기 채널과 가고 싶은 채널 간의 간격을 temp에 저장
    temp = abs(i - w)
    # min_value가 temp 보다 크면
    if min_value > temp:
        min_value = temp
        # temp를 저장한 min_value의 i 인덱스를 idx에 저장
        # 즐겨찾기 채널과 채널과의 간격이 가장 작을 때의 idx와
        # (c - w)를 서로 비교할 수 있다.
        idx = i
# (idx - w)에 1을 더해준 이유는 즐겨찾기 버튼을 한번 누른 수를 적용해야 하기 때문
print(min(abs(c - w), (abs(idx - w) + 1)))