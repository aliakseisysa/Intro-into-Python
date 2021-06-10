#. Программа принимает действительное положительное число x и целое отрицательное число y. Н
# еобходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). # При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
my_func = lambda a, b: a**b
print(my_func(10, -2))

def my_func_2(a, b):
    low_num = [a for el in range(1, abs(b))]
    proizved = a
    for el in low_num:
        proizved *= el
        res = 1/proizved
    return res
print(my_func_2(10, -2))
