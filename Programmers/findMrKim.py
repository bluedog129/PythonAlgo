seoul = ["Jane", "Kim"]

def solution(seoul):
    answer = ""

    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer += str(i)

    return "김서방은 " + answer + "에 있다"

print(solution(seoul))