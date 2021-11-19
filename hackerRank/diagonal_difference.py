arr = [[11, 2, 4],[4,5,6],[10,8,-12]]

def diagonalDifference(arr):
    right_diagonal_sum = 0
    left_diagonal_sum = 0

    for i in range(0, len(arr)):
        right_diagonal_sum += arr[i][i]
        left_diagonal_sum += arr[i][(len(arr)-1)-i]

    return abs(right_diagonal_sum - left_diagonal_sum)
    
print(diagonalDifference(arr))