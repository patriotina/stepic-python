def f(x):
    return x+1

n = int(input())
i = 1
d = {}
while i <= n:
    a = int(input())
    i += 1
    if a in d:
        print(d[a])
    else:
        d[a] = f(a)
        print(d[a])

