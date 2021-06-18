#1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
my_list = []
while True:
    my_line = input("Enter your data: ")
    if my_line == '':
        exit()
    else:
        newline = my_line + '\n'
        my_list.append(newline)
    with open("my_file1.txt", "w") as my_f_1:
        my_f_1.writelines(my_list)