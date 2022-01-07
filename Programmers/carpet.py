

def solution(brown, red):
    width = (brown + red) // 3
    height = 3
    
    while (width -2) * (height - 2) != red:
        width -= 1
        height = (brown + red) // width
        
    return [width, height]