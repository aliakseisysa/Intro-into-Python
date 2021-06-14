class Date:

    @classmethod
    def date_to_int(cls, my_date):
        my_list = my_date.split("-", )
        for el in my_list:
            print(int(el))

    @staticmethod
    def check_date(my_date):
        my_list = my_date.split("-", )

        if int(my_list[0]) > 32:
            print(f"In your date {my_date} you entered the impossible day num: {my_list[0]}")

        elif int(my_list[1]) > 12:
            print(f"In your date {my_date} you entered the impossible month num: {my_list[1]}")

        elif int(my_list[2]) > 2021:
            print(f"In your date {my_date} you entered the impossible year num: {my_list[2]}")

        else:
            print(f"You entered the correct date: {my_date}")


Date.date_to_int("11-01-2021")

Date.check_date("11-01-2021")

Date.check_date("45-01-2000")
Date.check_date("25-18-2000")
Date.check_date("25-12-2050")