# climbingLeaderboard
ranked = [100, 100, 50, 40, 20, 10]
players = [5, 25, 50, 120]
ranks = sorted(list(set(ranked)), reverse=True)

ranked_list=[]
for player in players:
    while ranks and player>=ranks[-1]:
        ranks.pop()
    ranked_list.append(len(ranks)+1)

print(ranked_list)
