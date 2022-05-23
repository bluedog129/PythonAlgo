words = input().upper()

unique_words = list(set(words))

words_cnt_list = []

for i in unique_words:
    cnt = words.count(i)
    words_cnt_list.append(cnt)

if words_cnt_list.count(max(words_cnt_list)) > 1:
    print('?')
else:
    max_index = words_cnt_list.index(max(words_cnt_list))
    print(unique_words[max_index])