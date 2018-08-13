s = input()

c = s.lower().count('c')
g = s.lower().count('g')

r = (c + g)/len(s)*100
print(r)