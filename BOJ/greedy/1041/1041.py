n = int(input())
dice_nums = list(map(int, input().split()))
result = 0
min_list = []

if n == 1:
    dice_nums.sort()
    for i in range(5):
        result += dice_nums[i]
else:
    min_list.append(min(dice_nums[0], dice_nums[5]))
    min_list.append(min(dice_nums[1], dice_nums[4]))
    min_list.append(min(dice_nums[2], dice_nums[3]))
    min_list.sort()

    one_min = min_list[0]
    two_min = min_list[0] + min_list[1]
    thr_min = min_list[0] + min_list[1] + min_list[2]

    one_side = 4 * (n - 2) * (n - 1) + (n - 2) * (n - 2)
    two_side = 4 * (n - 2) + 4 * (n - 1)
    thr_side = 4

    result = one_side * one_min + two_side * two_min + thr_side * thr_min

print(result)