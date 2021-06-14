class My_math(Exception):

    @staticmethod
    def my_divis(num_1, num_2):
        try:
            res = num_1 / num_2
            print(res)
        except ZeroDivisionError:
            print("На ноль делить нельзя")


My_math.my_divis(6, 2)
My_math.my_divis(0, 2)
My_math.my_divis(6, 0)