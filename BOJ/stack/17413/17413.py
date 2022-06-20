c_list = list(input())
result = ""
word = ""
flag = 0

for c in c_list:
    if flag == 0:
        if c == '<':
            flag = 1
            word += c
        # ' '만나면 한 번 끊음
        elif c == ' ':
            word += c
            result += word
            word = ""
        # 스택에 쌓음
        else:
            word = c + word

    elif flag == 1:
        word += c
        if c == '>':
            flag = 0
            result += word
            word = ""

print(result + word)



