'''


Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:

9 5 3
0 7 -1
-5 2 9
end

Sample Output 1:

3 21 22
10 6 19
20 16 -1

Sample Input 2:

1
end

Sample Output 2:

4


'''

#s = [int(i) for i in input().split()]

a = []
b = []
while True:
    b = input()
    if b != 'end':
        a.append([int(i) for i in b.split()])
    else:
        break

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i - 1][j] + a[i - len(a) + 1][j] + a[i][j - 1] + a[i][j - len(a[i]) + 1], end=' ')
    print()



"""
        if len(a) == 1:
            rli = rri = i
        else:

            if i == 0:
                rli = len(a)-1
                rri = i + 1
            elif i == len(a)-1:
                rli = i - 1
                rri = 0
            else:
                rli = i - 1
                rri = i + 1

            if j == 0:
                rlj = len(a[i])-1
                rrj = j + 1
            elif j == len(a[i])-1:
                rlj = j - 1
                rrj = 0
            else:
                rlj = j - 1
                rrj = j + 1

        print(a[rli][j] + a[rri][j] + a[i][rlj] + a[i][rrj], end=' ')
    print()
    
"""
    
#        print('for ', a[i][j], ' = ')
#        print(a[rli][j], end=' ')
#        print(a[rri][j], end=' ')
#        print(a[i][rlj], end=' ')
#        print(a[i][rrj])

#        rr.append(a[rli][j] + a[rri][j] + a[i][rlj] + a[i][rrj])
#    r.append(rr)
#    rr = []
