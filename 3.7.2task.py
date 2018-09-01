a1 = input()
a2 = input()
s1 = input()
s2 = input()
d = {}

i = 0
for aa in a1:
    d[aa] = a2[i]
    i += 1

inv_d = {value: key for key, value in d.items()}

r1 = ''
for ss in s1:
    r1 += d[ss]

print(r1)

r2 = ''
for ss in s2:
    r2 += inv_d[ss]
print(r2)
