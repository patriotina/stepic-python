i = 0
c = 0
while i < 5:
    print('*')
    c += 1
    if i % 2 == 0:
        print('**')
        c += 2
    if i > 2:
        print('***')
        c += 3
    i = i + 1
print(c)