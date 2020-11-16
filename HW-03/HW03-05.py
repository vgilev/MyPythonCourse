"""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""

sum_list_numbers = 0

"""Суммирование чисел и проверка букв в списке"""


def sum_numbers(list_numbers_action):
    global sum_list_numbers

    for number in list(list_numbers_action):

        try:

            int_number = int(number)

            sum_list_numbers += int_number

        except ValueError:

            print(f"Сумма введенных числе - {sum_list_numbers}. Вы ввели не только число, "
                  f"поэтому программа завершена!")

            exit()

    print(f"Сумма введенных числе - {sum_list_numbers}")


"""тут мы запрашиваем числа"""


def input_numbers():
    while True:
        list_numbers = input("Введите числа через пробел и нажмите Enter, "
                             "чтобы получить сумму и\или введите любую букву, чтобы завершить: ").split()

        sum_numbers(list_numbers)


input_numbers()
