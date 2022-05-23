string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    #find 함수를 이용하여 위치를 바로 반환
    print(string.find(i), end = ' ')