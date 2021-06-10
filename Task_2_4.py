my_words = input('Enter a bunch of words separated by space: ')
for ind, el in enumerate(my_words.split( ), 1):
    print(ind, el[1:11])