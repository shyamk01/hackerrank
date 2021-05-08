# climbingLeaderboard
ranked = [100, 100, 50, 40, 20, 10]
player = [5, 25, 50, 120]

def method_name(k):
    rank = 1
    rank_upd = [str(rank) + ":" + str(ranked[0])]
    for x in range(len(ranked)):
        if x < len(ranked) - 1:
            if ranked[x] == ranked[x + 1]:
                rank_upd.append(str(rank) + ":" + str(ranked[x + 1]))
                if x+1 == k:
                    print(rank)
            else:
                rank = rank + 1
                rank_upd.append(str(rank) + ":" + str(ranked[x + 1]))
                if x+1 == k:
                    print(rank)
    if k == 0:
        print(1)
    if k != -1:
        del rank_upd[k:k + 1]
        del ranked[k:k + 1]

for xp in range(len(player)):
    k = 0
    for x in range(len(ranked)):
        if player[xp] < ranked[x]:
            k = k + 1
            continue
        elif player[xp] > ranked[x]:
            k = x
            ranked.insert(x, player[xp])
            break
        elif player[xp] == ranked[x]:
            k = x + 1
            ranked.insert(x + 1, player[xp])
            break
    if k == len(ranked):
        ranked.insert(k + 1, player[xp])
    method_name(k)
