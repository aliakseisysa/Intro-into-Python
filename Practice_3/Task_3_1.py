#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_func():
    try:
        a_var = float(input("Enter the first number: "))
        b_var = float(input("Enter the second number: "))
    except ZeroDivisionError:
        return
    my_div = a_var / b_var
    return my_div
print(my_func())
