def minion_game(s):
    # your code goes here
    player1 = 0;
    player2 = 0;
    str_len = len(s)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 += (str_len) - i
            print("*"+str(player1))
        else:
            player2 += (str_len) - i
            print(player2)

    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart", player2)
    elif player1 == player2:
        print("Draw")
    else:
        print("Draw")
    # The Minion Game in Python - Hacker Rank Solution END


if __name__ == '__main__':
    minion_game("BANANA")