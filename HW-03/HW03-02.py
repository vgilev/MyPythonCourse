"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

info_list = {"Имя": "",
             "Фамилия": "",
             "Год рождения": "",
             "Город проживания": "",
             "Е-mail": "",
             "Телефон": ""
             }


def input_user(func_query_info):
    info_users = {}

    for info_list_name in info_list:
        input_users = input(f"Заполните поле '{info_list_name}' >>>")
        info_users[info_list_name] = input_users

    return info_users


all_user_info = input_user(info_list)

print(f"{all_user_info['Имя']} {all_user_info['Фамилия']}, год рождения: {all_user_info['Год рождения']}, "
      f"место проживания: {all_user_info['Город проживания']}. Контактная информация: {all_user_info['Е-mail']}, "
      f"телефон {all_user_info['Телефон']}")
