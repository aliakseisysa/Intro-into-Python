#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def max_func():
    var_1 = int(input("Enter the first number: "))
    var_2 = int(input("Enter the first number: "))
    var_3 = int(input("Enter the first number: "))
    my_list = [var_1, var_3, var_2]
    my_list.sort(reverse=True)
    my_sum = my_list[0]+my_list[1]
    return my_sum
print(max_func())