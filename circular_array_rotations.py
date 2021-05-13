from collections import deque
a=[1, 2, 3]
k=2
q=[0, 1, 2]
axc=deque(a)
axc.rotate(k)
ax=list(axc)
for a in q:
    print(ax[a])

