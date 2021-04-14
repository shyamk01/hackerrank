s = "08:05:45AM"
s =  "04:59:59AM"
a = s[-2:] # AM or PM
le = len(s)
s = s[0:le - 2]
tmsplt = s.split(":")
hr = int(tmsplt[0])
min = tmsplt[1]
sec = tmsplt[2]
if a == "PM":
    if hr!=12:
        hr1=12+hr
        print(str(hr1)+":"+str(min)+":"+str(sec))
    else:
        print(str(hr)+":"+str(min)+":"+str(sec))

else:
    if hr==12:
        hr1 = 12 - hr
        print(str(hr1).zfill(2) + ":" + str(min) + ":" + str(sec))
    else:
        print(str(hr).zfill(2) + ":" + str(min) + ":" + str(sec))



