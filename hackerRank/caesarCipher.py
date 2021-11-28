s = "There's-a-starman-waiting-in-the-sky"
k = 3

def caesarCipher(s, k):
    c = ""

    for i in s:
        if i.islower():
            c += chr((ord(i)-97+k)%26+97)
        elif i.isupper():
            c += chr((ord(i)-65+k)%26+65)
        else:
            c+=i
    return c

print(caesarCipher(s, k))