N_length =int(input("1이상 10이하인 수 중 이미지의 사이즈를 입력하세요: "))
K_multiple=int(input("1이하 10이하인 수 중 이미지를 늘릴 배수를 입력하세요: "))

list_b=[]
for i in range(N_length):             #행을 바꿔줌
    #int(input())
    list_i=[]

    # tmp=list(map(int, sys.stdin.readline().split()))
    print(i+2,"번째 줄의 요소를 입력하세요")
    for i in range(N_length):          #열을 바궈줌
        b=int(input("0,1중 원하는 숫자를 입력하세요: "))
        list_b.append(b)