''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT
arrstr = set()
def checkPatienceStatus(viruscompo, inpone):
    for pone in inpone:
        k = 0
        str = ""
        for i in range(len(pone)):
            for _ in range(len(viruscompo)):
                if k <= len(viruscompo) - 1 and pone[i] == viruscompo[k]:
                    str = str + pone[i]
                    break
                else:
                    k = k + 1

        if pone == str:
            arrstr.add("POSITIVE")
        else:
            arrstr.add("NEGATIVE")

    return arrstr


def main():
    viruscompo = input()
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = checkPatienceStatus(viruscompo, arr)
    for a in result:
        print(a)


main()

