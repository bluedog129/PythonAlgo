s = "))(()"


# 1 스택을 이용하는 방법
def solution(s):
    
    answer = True
    brackets = []

    for bracket in s:
        # bracket이 '('이면 brackets에 '('를 추가
        if bracket == '(':
            brackets.append(bracket)
        # bracket이 '('이 아닌 경우
        else:
            # brackets가 비어 있는 경우 false 
            # '('가 하나라도 brackets에 들어가지 않은 상태에서 
            # ')'이 들어가면 올바른 괄호가 될 수 없다.
            if brackets == []:
                answer = False
                break
            # bracket이 ')'인 경우 brackets의 '('를 pop한다.
            else:
                brackets.pop()
    # brackets 안에 '('가 하나라도 있다면 올바른 괄호가 아니다
    if brackets != []:
        answer = False
    
    return answer

print(solution(s))

# 2
def sol2(s):
    c = 0

    for x in s:
        if x == '(':
            c += 1
        else:
            c -= 1

        if c < 0:
            return False

    return c == 0

print(sol2(s))

# 3 
def is_pair(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

print(is_pair(s))





