s = [int(i) for i in input().split()]

s.sort()
vsp = s[0]
s.pop(0)
res = []
add = True
for i in s:
    if vsp == i:
        if add:
            res.append(i)
            add = False
    else:
        add = True
        vsp = i
for r in res:
    print(r)
