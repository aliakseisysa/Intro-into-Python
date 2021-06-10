#6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
from itertools import count
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle
my_list = input("Enter list els: ").split()
с = 0
for el in cycle(my_list):
    if с > 5:
        break
    print(el)
    с += 1

