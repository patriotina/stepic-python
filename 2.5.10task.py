s = [int(i) for i in input().split()]
res = []
if len(s) > 1:
    for i in range(len(s)):
        if i == 0:
            res.append(s[i+1] + s[len(s)-1])
        elif i == len(s) - 1:
            res.append(s[i - 1] + s[0])
        else:
            res.append(s[i+1] + s[i-1])
else:
    res = s
for r in res:
    print(r, end=' ')
