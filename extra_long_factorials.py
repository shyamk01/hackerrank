def factorial(n):
    t=1
    if n == 0:
        return 0
    answer =1
    while(n>=1):
        answer=answer*(n)
        print(answer)
        n = n - 1

    print(answer)


print(factorial(5))