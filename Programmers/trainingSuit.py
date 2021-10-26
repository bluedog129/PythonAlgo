n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생도 
    # 체육복을 도난 당했을 수 있을 경우를 위한 
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    return n-len(set_lost)

print(solution(n, lost, reserve))