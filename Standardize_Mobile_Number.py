def wrapper(f):
    def fun(l):
        l=map(int,l[-10:])
        l=sorted(l)
        l=map(str,l)
        for a in l:
            print("+91 " + a[-10:-5] + " " + a[-5:])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    x = ['09191919191', '9100256236', '+919593621456']
    sort_phone(x)
