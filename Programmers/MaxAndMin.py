s = "1 2 3 4"

def solution(s):
    max = -10000
    min = 10000

    answer = ''

    s_list = s.split(" ")

    for i in range(len(s_list)):
        if max < int(s_list[i]):
            max = int(s_list[i])
        if min > int(s_list[i]):
            min = int(s_list[i])
        
    answer += (str(min)+' ')
    answer += str(max)

    return answer

print(solution(s))

def solution(s):
    s_list=s.split(" ")
    n = [int(i) for i in s_list]
    n.sort()

    return str(n[0]) + " " + str(n[-1])

print(solution(s))