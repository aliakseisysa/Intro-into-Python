my_list = [7, 5, 3, 3, 2]
new_num = int(input('Enter any number: '))
max_num = my_list[0]
a = len(my_list)
min_num = my_list[a-1]
if new_num>max_num:
    my_list.insert(0, new_num)
    print(my_list)
elif new_num<min_num:
    my_list.append(new_num)
    print(my_list)
else:
    for i in range(a):
        if my_list[i] == new_num:
            my_list.insert(i+1, new_num)
            break
    print(my_list)