s = "bb"
tar = ([ord(char) - 96 for char in s.lower()])

for i in range(len(tar) - 1, 0, -1):
    if tar[i - 1] < tar[i]:
        break

if i == 1 and tar[i] <= tar[i - 1]:
    print("no answer")

x = tar[i - 1]
smallest = i

for j in range(i + 1, len(tar)):
    if x < tar[j] < tar[smallest]:
        smallest = j

tar[smallest],tar[i-1]=tar[i-1],tar[smallest]
num_bef=tar[0:i]
final_out = num_bef+ sorted(tar[i:])
st1=""
for x in range(len(final_out)):
    st1+=chr(ord('`')+final_out[x])
print(st1)