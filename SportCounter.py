distance = int(input("Введите кол-во километров за первый день >>>"))
plan_dist = int(input("Введите необходимое кол-во километров >>>"))

int_plan_dist = distance
print(f"1-й день: {distance}")
i = 1


while int_plan_dist <= plan_dist:
    i = i + 1

    int_plan_dist = round((int_plan_dist * 1.1),2)

    print(f"{i}-й день: {int_plan_dist}")

print(f"На {i}-й день спортсмен достиг результата не менее {plan_dist}")
