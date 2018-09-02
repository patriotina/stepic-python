n = int(input())
i = 0

x, y = 0, 0
while i < n:
    md, ms = input().split()
    if md == 'север':
        y += int(ms)
    elif md == 'юг':
        y -= int(ms)
    elif md == 'восток':
        x += int(ms)
    elif md == 'запад':
        x -= int(ms)
    i += 1
print(x)
print(y)