a = [1, 2, 3]
b = a
# значения списка b?
# 1,2,3
print(b)

a[1] = 10
# значения списка b?
# 1,10, 3
print(b)


b[0] = 20
# значения списка a?
# 20, 10, 3
print(a)

a = [5, 6]
# значения списка b?
# 20, 10, 3
print(b)