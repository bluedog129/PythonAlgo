from itertools import combinations


numbers = [2,1,3,4,1]

def solution(numbers):
    
    lst = list(combinations(numbers, 2))
    
    set_lst = set()
    
    for i in lst:
        a,b = i
        set_lst.add(a+b)
        
    result = list(set_lst)
    result.sort()
        
    return result

print(solution(numbers))