import sys

while True:
    str = sys.stdin.readline().rstrip()
    flag = 0
    stack = []

    if str == '.':
        break

    for c in str:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if not stack or stack[-1] == "[":
                print("no")
                flag = 1
                break
            else:
                stack.pop()
        elif c == "]":
            if not stack or stack[-1] == "(":
                print("no")
                flag = 1
                break
            else:
                stack.pop()

    if flag == 0:
        if not stack:
            print("yes")
        else:
            print("no")
