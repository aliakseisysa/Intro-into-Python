my_elements = input('Enter a bunch of words separated by space: ')
my_list = my_elements.split( )
print(f'This is my list: {my_list}')
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(f'This is my reversed list: {my_list}')
