skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

# 첫번째 방법
def sol1(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)

        for s in skill_tree:
            # s값이 skill 안의 값 중에서 있는지
            # s값이 skill_list 첫번째 값과 동일하지 않는지
            # 두가지 조건을 만족한다면 스킬트리 조건을 만족하지 않는다.
            if s in skill and s != skill_list.pop(0):
                break
        else:
            answer += 1

    return answer

print(sol1(skill, skill_trees))


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

# Queue를 이용해서 풀 수 있다.
from collections import deque

def sol2(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = deque(skill)
        for s in skill_tree:
            if s in skill and s != skill_list.popleft():
                break
        else:
            answer += 1

    return answer

print(sol1(skill, skill_trees))