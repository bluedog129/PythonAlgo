arr = [100, 200, 300]

def sum_all(arr):
    ret = 0
    for elem in arr:
        ret += elem
    return ret

print(sum_all(arr))