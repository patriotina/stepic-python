n = int(input())
print(n % 10)
print(n % 100)

if 0 <= n <= 1000:
    if (n % 10 == 1) and ((n % 100 <= 10) or (n % 100 >= 20)):
        print(n, 'программист')
    elif (2 <= (n % 10) <= 4) and ((n % 100 <= 10) or (n % 100 >= 20)):
        print(n, 'программиста')
    #elif ((n % 10 == 0) or (5 <= (n % 10) <= 9) and (n >= 20) or (n <= 10)) or (10 <= n <= 20):
    else:
        print(n, 'программистов')

"""
0 - прогиаммистов
1 - программист
2 - программиста
3 - программиста
4
5 - программистов
6 - программистов
7 - программистов
8 - программистов
9 - программистов
10 - программистов
11 
12
13
14
15
16
17
18
19
20
21 - программист
22 - программиста
23 - программиста
24 - программиста
25 - программистов
26 - программистов
27
28
29
30


"""