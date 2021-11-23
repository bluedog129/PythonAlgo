s = 'The Quick brown fox jumps over the lazy dog'

ascii_array = []
def pangrams(s):
    lower_string = s.lower()
    for i in range(len(lower_string)):
        # ord()로 s문자열을 아스키코드로 변환
        ascii_array.append(ord(lower_string[i]))

    # 영문 소문자 아스키코드는 97~122 까지 이루어져 있으므로 
    # 그 범위 만큼 ascii_array와 비교한다.
    for i in range(97, 123):
        if i not in ascii_array:
            return 'Not Pangram'

    return 'Pangram'

print(pangrams(s))

def pangrams(s):
    s = s.lower()
    s = set(s)
    s.discard(" ")
    return "pangram" if len(s) == 26 else "not pangram"

print(pangrams(s))