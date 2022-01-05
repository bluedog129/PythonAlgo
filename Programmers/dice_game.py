from itertools import product

monster = [4,9,5,8]
S1 = 2
S2 = 3
S3 = 4

def solution(monster, S1, S2, S3):
    p = product(range(S1), range(S2), range(S3))
    case = len([x for x in p if sum(x) + 4 not in monster])
    
    return int(case / (S1 * S2 * S3) * 1000)

print(solution(monster, S1, S2, S3))