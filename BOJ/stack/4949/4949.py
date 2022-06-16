# str_list = list(input().split("."))

while True:
    s = input()
    if s == '.':
        break

    flag = 0
    sum_a = 0
    sum_b = 0
    for c in s:
        if c == '(':
            sum_a += 1
        elif c == ')':
            sum_a -= 1
        if c == '[':
            sum_b += 1
        elif c == ']':
            sum_b -= 1
        if sum_a < 0 or sum_b < 0:
            print("no")
            flag = 1
            break

    if flag == 0:
        if sum_a > 0 or sum_b > 0:
            print("no")
        elif sum_a == 0 and sum_b == 0:
            print("yes")