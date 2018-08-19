s = [int(i) for i in input().split()]
n = int(input())
j = 0
c = 0
for ss in s:
    if ss == n:
        c += 1
        print(j, end=' ')
    j += 1
if c == 0:
    print('Отсутствует')
