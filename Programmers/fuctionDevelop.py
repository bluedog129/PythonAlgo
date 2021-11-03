progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    answer = []
    days = 1
    count = 0

    for i in range(len(progresses)):
        if i == 0 and progresses[i]+speeds[i]*days >= 100:
            count += 1
            answer.append(count)
        elif i > 0 and progresses[i]+speeds[i]*days >= 100:
            count += 1
            answer[-1] += 1
        while progresses[i]+speeds[i]*days < 100:
            days += 1
            if progresses[i]+speeds[i]*days >= 100:
                count = 1
                answer.append(count)
                break

    return answer

print(solution(progresses, speeds))