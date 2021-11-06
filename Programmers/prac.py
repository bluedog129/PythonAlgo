N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    result = {}
    denominator = len(stages)

    for stage in range(1, N+1):
        if denominator != 0:
            count = stage.count(stage)
            result[stage] = count / denominator
            denominator -= count
        
        else : 
            result[stage] = 0


    return 