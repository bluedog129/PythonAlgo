lottos = [44, 1, 0, 0, 31, 25]	
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    correct = 0
    zeroCount = lottos.count(0)

    for i in win_nums:
        if i in lottos:
            correct += 1

    return rank[correct+zeroCount], rank[correct]

print(solution(lottos, win_nums))