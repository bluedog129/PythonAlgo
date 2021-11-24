from functools import reduce

s = [2,2,1,3,2]
d = 4
m = 2

def add(a, b):
    return a+b

def birthday(s, d, m):

    count = 0

    for i in range(len(s)):
        temp_list = s[i:i+m] # 길이 m 만큼 부분배열 생성
        if reduce(add, temp_list) == d:
            count += 1
        
    return count

print(birthday(s, d, m))