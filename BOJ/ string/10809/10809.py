input_str = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_count = [-1 for i in range(0, 26)]

for i in range(len(input_str)):
    for j in range(len(alpha)):
        if input_str[i] == alpha[j]:
            if alpha_count[j] == -1:
                alpha_count[j] = i
            else:
                continue

for i in range(len(alpha_count)):
    print(alpha_count[i], end = ' ')