s = input().split()
print(s)
r = {}
for ss in s:
    ss = ss.lower()
    if ss in r:
        r[ss] += 1
    else:
        r[ss] = 1

for key, value in r.items():
    print(key, value)

