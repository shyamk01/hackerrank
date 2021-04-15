import re
from string import ascii_lowercase

s="We promptly judged antique ivory buckles for the next prize"
s=s.lower()
alphabet=sorted(set(ascii_lowercase))
s1=re.findall(r'\w',s)
if(set(alphabet).issubset(set(s1))):
    print("Pangrams")
else:
    print("Not Pangrams")
