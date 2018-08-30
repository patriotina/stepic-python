
def unzip(str):
    i = 1
    dig =''
    while i < len(str):
#    for ss in str:
        if str[i].isdigit():
            dig = dig + str[i]
#            print(str[i-1]*int(str[i]), end='')
        else:
            print(str[i - len(dig)-1]*int(dig), end='')
            dig=''
        i += 1
    print(str[i - len(dig)-1]*int(dig), end='')

with open('file.txt') as f:
    s = f.readline()
    unzip(s)
