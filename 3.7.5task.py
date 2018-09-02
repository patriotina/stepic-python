def scount(st):
    if not int(st[0]) in sdict:
        sdict[int(st[0])] = int(st[2].strip())
        sc[int(st[0])] = 1
    else:
        sdict[int(st[0])] += int(st[2].strip())
        sc[int(st[0])] += 1

i = 0
sdict = {}
sc = {}
with open('classes.txt') as f:
    for line in f:
        student = line.split('\t')
        scount(student)
        i += 1
print(i)
j = 1
print(sdict)

while j <= 11:

    if j in sdict:
        print(j, sdict[j] / sc[j])
    else:
        print(j, '-')
    j += 1
