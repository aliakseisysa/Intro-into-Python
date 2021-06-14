class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == '__main__':
    my_list = []

    while True:
        my_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")

        if my_input == "stop":
            break

        try:
            if not my_input.isdigit():
                raise NotNumberError(f"'{my_input}' has not numerical format")

            my_list.append(int(my_input))
        except NotNumberError as err:
            print(err)

    print(my_list)
