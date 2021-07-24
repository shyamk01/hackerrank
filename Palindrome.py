a = "madam"
flag = False
for i in range((len(a)-1//2)):
    if a[i] == a[len(a) - i-1]:
        pass
    else:
        flag = True
        break

if flag == True:
    print("Not Palindorm")
else:
    print("Palindrome")
