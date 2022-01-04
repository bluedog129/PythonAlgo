h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

def equalStacks(h1, h2, h3):
    # 리스트 역정렬
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]

    # 리스트의 합 
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    # pop
    while True:
        min_height = min(sum1, sum2, sum3)
        # base case
        if min_height == 0:
            return 0

        if min_height < sum1:
            sum1 -= h1.pop()
        if min_height < sum2:
            sum2 -= h2.pop()
        if min_height < sum3:
            sum3 -= h3.pop()

        if sum1 == sum2 == sum3:
            return sum1

print(equalStacks(h1, h2, h3))