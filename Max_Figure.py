number_in = int(input("Введите число больше 10 >>>"))

while True:

    if number_in < 10:

        number_in = int(input("Введите число больше 10 >>>"))

    else:

        number_list = list(str(number_in))

        print(max(number_list))

        break
