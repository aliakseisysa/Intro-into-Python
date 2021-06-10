#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def my_func(name_var, surname_var, y_birth_var, city_var, email_var, phone_var):
    print(f"Name: {name_var}, Surname: {surname_var}, Birth year: {y_birth_var}, City: {city_var}, Email: {email_var}, "
          f"Phone number: {phone_var})")
my_func(name_var = "Tom", surname_var = "Smith", y_birth_var = 1954, city_var = "Madrid", email_var = "tomsh@mail.com", phone_var = 7568708)
