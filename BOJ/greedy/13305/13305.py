n = int(input())
len_list = list(map(int, input().split()))
oil_list = list(map(int, input().split()))
result = 0

result += len_list[0] * oil_list[0]
min_oil = oil_list[0]

for i in range(1, len(len_list)):
    if min_oil > oil_list[i]:
        min_oil = oil_list[i]
        result += len_list[i] * min_oil
    else:
        result += len_list[i] * min_oil

print(result)


