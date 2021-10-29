a = 5
b = 24

def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = day*55
    pattern = [0,31,29,31,30,31,30,31,31,30,31,30,31]

    answer = day[sum(pattern[:a])+ b-1]

    return answer

print(solution(a, b))

def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
