a = int(input())
b = int(input())
c = int(input())
d = int(input())


print('', end = '\t')
for j in range(c, d+1):
    print(j, end = '\t')
print()
for i in range(a, b+1):
    for j in range(c, d+1):
        #if i == a: print(j * 1, end='\t')
        if j == c: print(i * 1, end='\t')
        print(i * j, end = '\t')
    print()

