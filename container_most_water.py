height = [1,1]
# area= max(height)*max(width)
# 1.max(value)* max(index)
# 2. max(value) -> count(2)

min_height=1
min_width=1
max_area=[]

from itertools import combinations
t=combinations(height,2)
for i in range(len(height)):
    for j in range(len(height)):
        if j+1 <len(height):
            dis=j+1-i
            if dis>0:
                min_h=min(height[i],height[j+1])
                area=min_h*dis
                max_area.append(area)

print(max(max_area))


