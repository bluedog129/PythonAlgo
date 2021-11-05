phone_number = "01033334444"

def solution(phone_number):
    num = len(phone_number)
    back = phone_number[-4:]
    

    return "*"*(num-4)+back

print(solution(phone_number))