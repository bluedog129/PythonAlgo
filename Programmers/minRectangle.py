sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    answer = 0
    sizes = [sorted(size, reverse=True) for size in sizes]

    width = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]

    width, heights = max(width), max(heights)

    answer = width * heights

    return answer

print(solution(sizes))

def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

print(solution(sizes))