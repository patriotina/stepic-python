#a, b = (int(i) for i in input().split())
a = int(input())
b = int(input())
for i in range(0, 3):
    if a % 3 == 0:
        break
    a = a + 1
s = 0
d = 0
for i in range(a, b+1, 3):
    s = s + i
    d = d + 1
print(s/d)

