s = input()

st = s[0]
c = 0
r = ''
for i in s:
    if i == st:
        c = c + 1
    else:
        r = r + st + str(c)
        c = 1
        st = i
r = r + st + str(c)
print(r)