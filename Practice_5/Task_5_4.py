#. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("my_file4_2.txt", "w") as f_obj:
    my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

    with open("my_file4.txt") as my_f_obj:
        for line in my_f_obj:
            my_list = line.split()
            keys = my_list[0]
            values = my_list[2]
            my_dict_2 = {keys:values}
            for key in my_dict_2:
                print(f"{my_dict.get(key)} - {my_dict_2.get(key)}")
                print(f"{my_dict.get(key)} - {my_dict_2.get(key)}", file=f_obj)
