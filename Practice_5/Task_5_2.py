#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("my_file2.txt") as my_f_obj:
    lines_num = 0
    for line in my_f_obj:
        lines_num += 1
        words = len(line.split(' '))
        print(f"The number of words in the line is: {words}")
print(f"The number of lines in your file is: {lines_num}")