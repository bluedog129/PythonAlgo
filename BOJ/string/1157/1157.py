words = input().upper()
# 단어안의 중복되는 문자를 제거
unique_words = list(set(words))

cnt_list = []
for x in unique_words:
    # words안 x문자의 갯수
    cnt = words.count(x)
    # x문자의 갯수를 cnt_list에 넣는다.
    cnt_list.append(cnt)

    # cnt_list(x문자 각각의 갯수)의 최대값이 cnt_list안에 중복된다면
    # '?' 반환
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
    # 위의 조건에 들어가지 않는다면
    # cnt_list의 최대값이 들어있는 인덱스를 구하고 출력
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])
