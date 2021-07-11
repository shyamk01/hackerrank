# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

def person_lister(f):
    def inner(people):
        tx=sorted(people,key=lambda x:int(x[2]),reverse=False)
        for a in tx:
            if a[-1]=='M':
                 print("Mr. "+ str(a[0]+" "+a[1]))
            else:
                 print("Ms. " + str(a[0]+" "+a[1]))

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    x=[
        ['Jake', 'Jake', '42', 'M'], ['Jake', 'Kevin', '57', 'M'], ['Jake', 'Michael', '91', 'M'],
        ['Kevin', 'Jake', '2', 'M'], ['Kevin', 'Kevin', '44', 'M'], ['Kevin', 'Michael', '100', 'M'],
        ['Michael', 'Jake', '4', 'M'], ['Michael', 'Kevin', '36', 'M'], ['Michael', 'Michael', '15', 'M'],
        ['Michael', 'Michael', '6', 'M']
       ]
    print(name_format(x), sep='\n')