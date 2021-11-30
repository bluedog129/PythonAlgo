s = "Zbcdefg"

def solution(s):
    s = list(s)

    s.sort(reverse=True)

    return "".join(s)

print(solution(s))