user_number = int(input("Enter any positive integer number: "))
max_number = 0
while user_number > 0:
    last_number = user_number % 10
    if last_number >= max_number:
        max_number = last_number
        print(max_number)
    if last_number < max_number:
        print(max_number)
    user_number //= 10