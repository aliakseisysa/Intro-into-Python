#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.
def my_func():
    try:
        my_sum = 0
        while True:
            def my_int_func():
                nums = input("Enter space seperated numbers or special sign 'q': ")
                nums = nums.split()
                nonlocal my_sum
                for i in range(len(nums)):
                    my_sum += float(nums[i])
                return my_sum
            print(my_int_func())
    except:
        nums() == "q"
        return 'quit'
print(my_func())
