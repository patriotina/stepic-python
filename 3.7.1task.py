# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
def add_score(c1, s1, c2, s2):
    if not c1 in d:
        d[c1] = [0, 0, 0, 0, 0]
    if not c2 in d:
        d[c2] = [0, 0, 0, 0, 0]
    d[c1][0] += 1
    d[c2][0] += 1
    if s1 > s2:
        d[c1][1] += 1
        d[c2][3] += 1
        d[c1][4] += 3
    elif s1 == s2:
        d[c1][2] += 1
        d[c2][2] += 1
        d[c1][4] += 1
        d[c2][4] += 1
    else:
        d[c1][3] += 1
        d[c2][1] += 1
        d[c2][4] += 3

n = int(input())
i = 0
d = {}
while i < n:
    s = input()
    ss = s.split(';')
    add_score(ss[0], ss[1], ss[2], ss[3])
    i += 1

for key, value in d.items():
    print(key + ':', end='')
    for v in value:
        print(v, end=' ')
    print()