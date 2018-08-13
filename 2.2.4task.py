a = 1

while a > 0:
    i = int(input())
    if i < 10:
        continue
    elif i > 100:
        break
    else:
        print(i)