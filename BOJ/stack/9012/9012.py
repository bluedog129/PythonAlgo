t = int(input())

def vps(s_list):
    sum = 0
    for i in s_list:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            return"NO"

    if sum > 0:
        return "NO"
    elif sum == 0:
        return "YES"

for _ in range(t):
    s_list = list(input())

    print(vps(s_list))