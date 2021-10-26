stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5

def solution(N, stages):
    result = {}
    denominator = len(stages)

    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count

        else :
            result[stage] = 0

    return sorted(result, key = lambda x : result[x], reverse=True)

print(solution(N, stages))