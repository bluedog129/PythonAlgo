s = "PoooyY"

def solution(s):
    answer = True

    s = s.lower()

    count_p = s.count_list('p')
    count_y = s.count_list('y')

    if count_p == 0 and count_y == 0:
        return True
    
    if count_p == count_y:
        return True

    return False

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count_list('p') == s.lower().count_list('y')

print(solution(s))