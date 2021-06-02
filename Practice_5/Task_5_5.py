#5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.
with open("my_file5.txt", "w+") as f_obj:
    print(input("Input space seperated numbers: "), file=f_obj)

with open("my_file5.txt") as my_f_obj:
    for line in my_f_obj:
        my_list = line.split()
        my_sum = 0
        for i in range(len(my_list)):
            my_sum += float(my_list[i])
        print(f"The sum of numbers is: {my_sum}")
