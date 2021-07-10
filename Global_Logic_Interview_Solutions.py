# Consider to use:
#   - different data structures: dictionary, set, list
#   - build-in functions: map, zip, sorted, etc.
#   - lambda expressions
#   - string functions: split, join, etc.
#
# Example of input text: ‘aaa bb bbb cc ccc cc aaa bb aaa cc aaa’
# Expected result: 1|3|4|2|5|2|1|3|1|2|1
#              or: 1|3|5|2|4|2|1|3|1|2|1
# Codes table (<word>,<occurence>,<code>): [('aaa', 4, 1), ('cc', 3, 2), ('bb', 2, 3), ('ccc', 1, 4), ('bbb', 1, 5)]

#.       1|  3| 4|. 2| 5|. 2| 1|. 3| 1|  2| 1
text = 'aaa bb bbb cc ccc cc aaa bb aaa cc aaa'

st=set()
a=text.split(" ")
z=set(a)
za={}
final=""
za1={}
cnt=0
for az in z:
    za[az]=a.count(az)
at=sorted(za,key=lambda x:za[x],reverse=True)
for atz in at:
    za1[atz]=cnt+1
    cnt=cnt+1
for art in a:
   final+=str(za1[art])
print(final)

