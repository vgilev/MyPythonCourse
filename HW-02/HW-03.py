dict_time_year = {"winter": (1, 2, 12), "spring": (3, 4, 5), "summer": (6, 7, 8), "autumn": (9, 10, 11)}

print(dict_time_year)

month = int(input("Введите число "))

# вывод из словаря
for k in dict_time_year.keys():
    if month in dict_time_year[k]:
        print(k)
