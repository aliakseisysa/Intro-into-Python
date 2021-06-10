#2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
from random import randint
my_list = [randint(0, 100) for i in range(10)]
new_list = []
for i in range(len(my_list)-1):
    if my_list[i+1] > my_list[i]:
        new_list.append(my_list[i+1])
print(my_list)
print(new_list)

