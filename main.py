import re
def minion_game(s):
    isalpha =s.isalpha()
    if isalpha==False:
        exit()
    vow="AEIOU"
    kevin=[]
    stuart=[]
    a=range(0,len(s)+1)
    for l in a:
        for j in a:

            if s[l:j]!= "":
                if s[l:j][0].lower() in vow.lower():
                    kevin.append(s[l:j])
                else:
                    stuart.append(s[l:j])

    if len(kevin)>len(stuart):
        print("Kevin " + str(len(kevin)))
    elif len(kevin)<len(stuart):
        print("Stuart " + str(len(stuart)))
    else:
        print("Draw")

if __name__ == '__main__':
    minion_game("BANANA")