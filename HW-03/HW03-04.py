"""Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
в виде функции my_func(x, y). При решении задания необходимо обойтись
без встроенной функции возведения числа в степень."""


def my_func(arg1, arg2):
    global extent_args

    extent_args = arg1 ** arg2

    return extent_args


def my_func2(arg1_1, arg2_2):
    global extent_args2
    extent_args2 = 1

    for i in range(abs(arg2_2)):

        extent_args2 *= arg1_1

        if arg2_2>=0:
            return extent_args2
        else:
            return 1/extent_args2


numb1 = int(input("Введите положительное число: "))
numb2 = int(input("Введите целое отрицательное число: "))

extent_args = my_func(numb1, numb2)
extent_args2 = my_func(numb1, numb2)

print(f"Вариант 1: Число {numb1} в степени {numb2} равно {extent_args} ")
print(f"Вариант 2: Число {numb1} в степени {numb2} равно {extent_args2} ")
