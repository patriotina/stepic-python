#Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value

#Если ключ key
#есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
#Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2⋅key. Если и ключа 2⋅key нет, то нужно добавить ключ 2⋅key в словарь и сопоставить ему список из переданного элемента [value]

#Требуется реализовать только эту функцию, кода вне неё не должно быть.
#Функция не должна вызывать внутри себя функции input и print.

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        if key*2 in d:
            d[key*2].append(value)
        else:
            d[key*2] = []
            d[key*2].append(value)
    print(d)



update_dictionary({1:[123], 5:[222], 3:[332]}, 2, 443)