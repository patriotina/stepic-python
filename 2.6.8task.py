

n = int(input())

sc = 1
num = 1
for i in range(n):
    print(num, end = ' ')
    sc += 1
    if sc > num:
        sc = 1
        num += 1


