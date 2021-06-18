#6. Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических
# и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
subjects = {}

with open("my_file6.txt") as subs:
    lines = subs.readlines()

for line in lines:
    data = line.replace('(', ' ').split()
    print((data))
    print(data[0][:-1])
    subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())

print(subjects)

