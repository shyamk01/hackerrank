'''
Prime Game (100 Marks)
Rax, a school student, was bored at home in the pandemic. He wanted to play but there was no one to play with. He was doing some mathematics questions including prime numbers and thought of creating a game using the same. After a few days of work, he was ready with his game. He wants to play the game with you.

GAME:

Rax will randomly provide you a range [ L , R ] (both inclusive) and you have to tell him the maximum difference between the prime numbers in the given range. There are three answers possible for the given range.

There are two distinct prime numbers in the given range so the maximum difference can be found.

There is only one distinct prime number in the given range. The maximum difference in this case would be 0.

There are no prime numbers in the given range. The output for this case would be -1.

To win the game, the participant should answer the prime difference correctly for the given range.

Example:

Range: [ 1, 10 ]

The maximum difference between the prime numbers in the given range is 5.

Difference = 7 - 2 = 5

Range: [ 5, 5 ]

There is only one distinct prime number so the maximum difference would be 0.

Range: [ 8 , 10 ]

There is no prime number in the given range so the output for the given range would be -1.

Can you win the game?

Input Format
The first line of input consists of the number of test cases, T

Next T lines each consists of two space-separated integers, L and R

Constraints
1<= T <=10

2<= L<= R<=10^6

Output Format
For each test case, print the maximum difference in the given range in a separate line.

Sample TestCase 1
Input
5
5 5
2 7
8 10
10 20
4 5
Output
0
5
-1
8
0
Explanation

Test Case 1: [ 5 - 2 ] = 3

Test Case 2: [ 7 - 2 ] = 5

Test Case 3: No prime number in the given range. Output = -1

Test Case 4: [ 19 - 11 ] = 8

Test Case 5: The difference would be 0 since there is only one prime number in the given range.
'''

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