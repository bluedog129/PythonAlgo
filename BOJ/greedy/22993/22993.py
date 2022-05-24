n = int(input())
player_list = list(map(int, input().split()))

jun = player_list.pop(0)

player_list.sort()

for player in player_list:
    if player >= jun:
        print("No")
        exit()
    else:
        jun += player

print("Yes")