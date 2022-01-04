stack = []
# 입력받은 정수형 값 만큼 반복
for _ in range(int(input())):
    # int형으로 입력값을 받되 띄어쓰기나 , 등의 구분을 하지 않고 입력 받음
    q = list(map(int, input().split( )))

    if q[0] == 1:
        # 스택이 비어있을 경우와 아닐경우 구분
        if stack:
            # 스택이 비어있으면 
            stack.append(max(stack[-1], q[1]))
        else:
            stack.append(q[1])
    
    elif q[0] == 2:
        stack.pop()
    else:
        print(stack[-1])

# 의문 
# 1번은 스택에 요소를 푸쉬하는 건데 왜 굳이 스택이 비어있을 경우와 
# 아닐경우를 구분하는건지 이해가 안 된다
# 그리고 3번은 최대값을 출력하라고 했는데 
# 왜 스택의 마지막 값을 넣어야 통과가 되는 것인가???

# 얻은 지식 
# 1. 입력받은 정수형 값 만큼 반복 
# for _ in range(int(input())):
# 2. list가 비어있으면 false 요소가 하나라도 있으면 true