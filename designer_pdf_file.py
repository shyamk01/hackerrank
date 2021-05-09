h=[1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word='zxy'

from string import ascii_lowercase
letters = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}
ax=[]
for a in word:
    if a in letters:
        ax.append(h[letters[a]-1])

print(len(word)*max(ax))



