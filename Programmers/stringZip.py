s = "abcabcabcabcdededededede"

def solution(s):
    answer = len(s)

    for size in range(1, len(s) // 2 + 1):
        count = 1
        compress = 0
        
        prev = s[:size]
        for i in range(size, len(s) + size, size):
            curr = s[i:i + size]
            if prev == curr:
                count += 1
            else:
                compress += size + len(str(count)) if 1 < count else len(prev)
                prev = curr
                count = 1
        answer = min(answer, compress)

    return answer

print(solution(s))