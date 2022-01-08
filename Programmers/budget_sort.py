d = [1,3,2,5,4]
budget = 9

def solution1(d, budget):
    answer = 0
    d_sum = 0
    d.sort()

    for d_list in d:
        d_sum += d_list

        if d_sum <= budget:
            answer += 1


    return answer

def solution2(d, budget):
    answer = 0
    price_sum = 0
    
    for price in sorted(d): # 부서별 신청한 금액을 오름차순 정렬합니다.
        price_sum += price # 예산을 더해주고
        if price_sum > budget: # 예산을 초과하면
            break # 종료!!
        answer += 1
        
    return answer # 가능한 부서를 리턴합니다.

print(solution1(d, budget), solution2(d, budget))