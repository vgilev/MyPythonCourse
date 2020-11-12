change_list = list(input("Введите несколько любых символов"))

print(change_list)

for i in range(0, len(change_list)-1, 2):

    change_list[i], change_list[i + 1] = change_list[i + 1], change_list[i]

print(change_list)
