def checkPatienceStatus(viruscompo, inpone):
    arrstr = []
    flag = 0
    for pone in inpone:
        k = 0
        str = ""
        for i in range(len(pone)):
            if set(pone).issubset(set(viruscompo)):
                for _ in range(len(viruscompo)):
                    if k <= len(viruscompo) - 1 and pone[i] == viruscompo[k]:
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
    viruscompo="coronavirus"
    ipone=set()
    ipone.add("onarous")
    print(checkPatienceStatus(viruscompo, ipone))
    # viruscompo = input()
    # n = int(input())
    # arr = []
    # for _ in range(n):
    #     arr_item = input()
    #     arr.append(arr_item)
    # result = checkPatienceStatus(viruscompo, arr)
    # [print(a) for a in result]


main()