"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""

str_result = ""
result_words = []

"""Делаем первую букву заглавной"""


def int_func(words):
    global str_result

    for word in words:
        result_words.append(word.capitalize())

        str_result = ' '.join(result_words)

    # print(result_words)
    print(str_result)


list_words = input("Введите одно слово или несколько слов через пробел: ").split()

# print(list_words)

int_func(list_words)
