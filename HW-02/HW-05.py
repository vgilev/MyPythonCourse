rate = [15, 12, 12, 10, 7, 5, 3, 3, 2]
print(rate)

numbers = int(input("Введите число "))

rate.append(numbers)

rate.sort(reverse=True)

print(rate)
