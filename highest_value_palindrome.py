def highestValuePalindrome(s, n, k):
    j=0
    v=n-1
    c=0
    s=[int(v) for v in s]
    a=[0]*n
    while j<n//2:
        # If the value of the front and back is not equal then set the value of max in the front one
        if s[j]!=s[v]:
            c=c+1
            s[j]=max(s[j],s[v])
            s[v]=s[j]
            a[j]=1
        j=j+1
        v=v-1
        # If the count of the change's index value of the array is greater then the what the value provided by input,
        # then we the string is not palindrome
        if c>k:
            return '-1'
    if c<k:
        m=k-c
        l=n//2
        for j in range(l):
            if a[j]==1:
                if s[j]!=9:
                    m=m-1
                    s[j]=9
            elif a[j]==0 and m>=2:
                if s[j]!=9:
                    m=m-2
                    s[j]=9
            if m==0:
                break
        print(s,a)
        # check the string length is not integer and still have the value(m), to replace with maximum digit
        if n%2!=0:
            if m>0:
                s[n//2]=9
            s=s[:l+1]+s[:l][::-1]
        else:
            s=s[:l]+s[:l][::-1]
        print(s)
    return "".join(map(str,s))

s="99341"

print(highestValuePalindrome("3943", 4, 4))