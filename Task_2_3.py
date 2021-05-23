#List solution
my_list_seasons = ["Winter", "Winter", "Spring", "Spring", "Spring",
                   "Summer", "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter"]
months_num = int(input('Enter the months number: '))
print(my_list_seasons[months_num-1])

#Dictionary solution
my_dict_seasons = {1:"Winter", 2:"Winter", 3:"Spring", 4:"Spring", 5:"Spring",
                   6:"Summer", 7:"Summer", 8:"Summer", 9:"Autumn", 10:"Autumn", 11:"Autumn", 12:"Winter"}
months_num = int(input('Enter the months number: '))
print(my_dict_seasons.get(months_num))
