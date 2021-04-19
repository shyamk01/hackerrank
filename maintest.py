viruscompo = "coronavirus"
pone = "abcde"  # NEGATIVE
#pone="crnas" #POSITIVE
# pone="onarous" #NEGATIVE
''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT

def checkPatienceStatus(viruscompo, inpone):
    arrstr = []
    flag = 0
    for pone in inpone:
        k = 0
        str = ""
        for i in range(len(pone)):
            for _ in range(len(viruscompo)):
                if set(pone).issubset(set(viruscompo)):
                    flag = 1
                else:
                    break
                if k <= len(viruscompo) - 1 and pone[i] == viruscompo[k] and flag == 1:
                    str = str + pone[i]
                    break
                else:
                    k = k + 1

        if pone == str:
            arrstr.append("POSITIVE")
        elif flag == 0:
            arrstr.append("NEGATIVE")

        else:
            arrstr.append("NEGATIVE")
    return arrstr


def main():
    viruscompo = input()
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = checkPatienceStatus(viruscompo, arr)
    [print(a) for a in result]


main()

