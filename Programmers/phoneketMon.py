nums = [3,1,2,3]

def solution(nums):
    answer = 0
    # 고를 수 있는 포켓몬의 수
    pick = len(nums) / 2
    # nums를 집합 자료형으로 변환하여 중복제거 후 다시 
    # 리스트 변환
    nums = list(set(nums))
    # 중복을 제거한 nums의 길이가 pick과 크거나 같으면
    # 가질 수 있는 최대 종류는 pick과 같다.
    if len(nums) >= pick:
        answer = pick
    # nums의 길이가 작은 경우 그 만큼의 종류를 가질 수 있다.
    elif len(nums) < pick:
        answer = len(nums)

    return answer

print(solution(nums))