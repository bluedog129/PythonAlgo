n = 3

def flippingBits(n):
    result = 0
    # 30 ~ -1 까지 내림 탐색
    for i in range(31, -1, -1):
        # 주어진 n에 2의 i제곱을 나누어서 1이 되는 조건
        if n//(2**i) == 1:
            n = n - 2**i
            x = 0
        # 나누어서 1이 되지 않는 조건
        else :
            x = 1

        # 결과값 리턴
        result += 2**i * x

    return result

print(flippingBits(n))