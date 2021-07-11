def wrapper(f):
    def fun(l):
        res = [int(x[-10:]) for x in l]
        l=sorted(res)
        l=map(str,l)
        for a in l:
            print("+91 " + a[-10:-5] + " " + a[-5:])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    x = ['08915625469', '+918756954120']
    sort_phone(x)
