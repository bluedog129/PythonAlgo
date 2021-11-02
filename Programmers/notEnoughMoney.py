price = 3
money = 20
count = 4

def solution(price, money, count):
    answer = 0
    original_price = price

    for i in range(1, count+1):
        money -= price
        price += original_price
    
    if money < 0:
        answer = money * (-1)
    
    return answer
    
print(solution(price, money, count))