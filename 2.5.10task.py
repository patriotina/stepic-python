s = [int(i) for i in input().split()]
res = []
for i in range(len(s)):
    res.append(s[i:i+1] + s[i: i-1])
print(res)
3