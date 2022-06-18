from itertools import combinations
new_name="aba"
old_name="ababa"

# new_name="ccc"
# old_name="cccc"
count=0
comb =combinations(old_name,len(new_name))
for i in list(comb):
    if ''.join(map(str,i))==new_name:
        count+=1
print(count)