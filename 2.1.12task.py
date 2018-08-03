a = int(input())
b = int(input())
d = 1
while d <= a * b:
    if (d % a == 0) and (d % b == 0):
        print(d)
        exit()
    d += 1
