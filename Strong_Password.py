import re

password = "AUzs-nV"
n = 6

cnt = 0
if not re.compile('[0-9]').search(password):
    cnt += 1
if not re.compile('[a-z]').search(password):
    cnt += 1
if not re.compile('[A-Z]').search(password):
    cnt += 1
if not re.compile('[!@#$%^&*()-+]').search(password):
    cnt += 1
if len(password) < n:
    cnt += 1
if len(password) < 6 and cnt + n < 6:
    cnt += 6 - (len(password) + cnt)
print(cnt)
