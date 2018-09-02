d = int(input())
i = 0
di = []
while i < d:
    di.append(input().lower())
    i += 1
i = 0
l = int(input())
s = []
while i < l:
    s.append(input().lower().split())
    i += 1

mdi = set()
for sline in s:
    for word in sline:
        if not word in di:
            mdi.add(word)

for md in mdi:
    print(md)
#print(di)
#print(s)
