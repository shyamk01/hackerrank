''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
def checkprime(m, n):
    arrprime = set()
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    for p in range(m, n+1):
        if prime[p]:
            arrprime.add(p)

    if arrprime == set():
        print("-1")
    elif len(arrprime) == 1:
        print("0")
    else:
        min1 = min(arrprime)
        max1 = max(arrprime)
        print(max1 - min1)

def main():
    n = int(input())
    for _ in range(0,n):
        lowupp=input()
        loup=lowupp.split(" ")
        checkprime(int(loup[0]), int(loup[1]))

main()

