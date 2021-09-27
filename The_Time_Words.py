def timeInWords(h, m):
    # Write your code here
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
    two_digits = ["ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen", "twenty"]

    s = ""
    sw = ""
    hs = ""
    if m > 30:
        h = h + 1

    if len(str(h)) < 2:
        hs = single_digits[h]
    else:
        t = h - 10
        hs = two_digits[t]

    if m == 00:
        s = "o' clock"
    elif 00 < m < 9:
        s = "minute past"
    elif 9 < m < 30 and m != 15:
        s = "minutes past"
    elif m == 30:
        s = "half past"
    elif m == 45:
        s = "quarter to"
    elif m == 15:
        s = "quarter past"
    else:
        s = "minutes to"

    if m > 30:
        m = 60 - m

    if len(str(m)) > 1:
        if 10 <= m <= 20 and m != 15:
            ms = abs(10 - m)
            sw = two_digits[ms]
        if m > 20 and m != 15 and m != 30:
            ms = 10
            dou = abs(m - 20)
            sw = two_digits[ms] + " " + single_digits[dou]
    if len(str(m)) == 1 and m != 00:
        sw = single_digits[m]

    if m == 00:
        return (hs.strip() + " " + s.strip()).strip()
    else:
        return (sw.strip() + " " + s.strip() + " " + hs.strip()).strip()

h=10
m=57
print(timeInWords(h, m))