s = "3people unFollowed me"

def solution(s):
    s = s.lower()
    s_list = s.split(' ')

    for i in range(len(s_list)):
        s_list[i] = s_list[i].capitalize()
            
    return " ".join(s_list)

print(solution(s))


def Jaden_Case(s):
    # 이 문제를 한방에 해결해주는 함수 ㅋㅋㅋㅋ
    return s.title()

print(solution(s))