revenue = int(input("Введите выручку за период >>>"))
cost = int(input("Введите издержки за тот же период >>>"))

fin_result = revenue - cost

if fin_result < 0:

    print("Вы работаете в убыток")

else:

    rent = fin_result / revenue * 100

    print(f"Вы работаете с прибылью! Рентабельность - {rent}%")

    count_personal = int(input("Введите количество сотрудников >>>"))

    rent_one_pers = fin_result / count_personal

    print(f"Прибыль на одного сотрудника - {rent_one_pers}")
