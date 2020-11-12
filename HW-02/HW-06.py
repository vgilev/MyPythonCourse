tuple_dict = []
dict_value = {"name": "", "cost": "", "quantity": "", "unit": ""}  # номер и словарь

count_product = int(input("Введите количество наименований товаров (например, 3): "))

i = 0

while i != count_product:
    i += 1

    _list = input("Введите сведения о товарах через пробел: название, цена, количество, ед.измерения ")

    _dict = _list.split(" ")

    dict_value = dict(name=_dict[0], cost=_dict[1], quantity=_dict[2], unit=_dict[3])

    tuple_dict.append(i)
    tuple_dict.append(dict_value)

print(tuple_dict)
