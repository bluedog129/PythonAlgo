a = [1,2,3,4,3,2,1]

def lonelyinteger(a):
    for i in range(0,len(a)):
        if a.count_list(a[i]) == 1:
            return a[i]


print(lonelyinteger(a))