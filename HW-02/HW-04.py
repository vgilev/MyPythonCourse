_list = input("Введите несколько слов через пробел ")

change_list = _list.split(" ")

print(change_list)

i = 0

for k in change_list:
    i += 1
    print(f"{i}. {k[0:10]}")

