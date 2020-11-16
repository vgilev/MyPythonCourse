"""Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов."""


def my_func(arg1, arg2, arg3):

    sum_max_args = arg1+arg2+arg3-min(arg1, arg2, arg3)

    print(f"Сумма двух максимальных значений равна - {sum_max_args}")


numb1 = int(input("Введите первое число: "))
numb2 = int(input("Введите второе число: "))
numb3 = int(input("Введите третье число: "))

my_func(numb1, numb2, numb3)

