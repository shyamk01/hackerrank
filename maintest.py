import string
inparr = ['abcdde', 'baccd', 'eeabg']
#inparr = ['abc', 'abc', 'bc']
alphabet_string = string. ascii_lowercase
alphabet_list = list(alphabet_string)
arr=[]
for ax in alphabet_list:
    str=""
    for x in range(len(inparr)):
        if ax in inparr[x]:
            str=str+ax
        else:
            str = ""
            break;
    if str!="":
        arr.append(str)

print(len(arr))
