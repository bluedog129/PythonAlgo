participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


# 1. 단순 반복으로 푸는 풀이
def sol1(participant, completion):
    for i in completion: # O(n)
        participant.remove(i) # O(n)
    return str(participant[0])

print(sol1(participant, completion))

# 2. 정렬을 이용해서 푸는 풀이
def solution(participant, completion):
    answer = ""

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[len(participant)-1]

print(solution(participant, completion))

# 3. 파이썬 Built-in 함수를 이용한 풀이
# Counter를 이용한 풀이

from collections import Counter

def sol3(participant, completion):
    result = Counter(participant) - Counter(completion)

    return list(result.keys())[0]

print(sol3(participant, completion))