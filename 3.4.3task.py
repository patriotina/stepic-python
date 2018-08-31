
def countFromLine(s):
    for ss in s:
        ss = ss.lower()
        if ss in r:
            r[ss] += 1
        else:
            r[ss] = 1

def findMax(d):
    max = 0
    kmax = ''
    for dkey, dval in d.items():
        if dval > max:
            max = dval
            kmax = dkey
    print(kmax, max)

r = {}
with open('file343.txt') as f:
    fl = f.read().replace('\n', ' ').lower().split()
    countFromLine(fl)

findMax(r)

