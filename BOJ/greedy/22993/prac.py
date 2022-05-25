n = int(input())
player_list = list(map(int, input().split()))

jun = player_list.pop(0)

player_list.sort()

for player in player_list:
    if player >= jun:
        break
    else:
        jun += player

result = ""

# 이부분
if jun > player_list[len(player_list) - 1]:
    result = "Yes"
else:
    result = "No"

print(result)