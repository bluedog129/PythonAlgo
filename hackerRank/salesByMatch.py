n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

def sockMerchant(n, ar):
    ar_set = 0
    ar_count = 0
    
    ar_set = set(ar)

    for i in ar_set:
        ar_count += ar.count_list(i) // 2

    return ar_count

print(sockMerchant(n, ar))