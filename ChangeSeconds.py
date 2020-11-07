seconds = int(input("Введите время в секундах >>>"))

time_in_hours = seconds // 3600
time_in_minutes = (seconds - time_in_hours * 3600) // 60
time_in_seconds = seconds - (time_in_hours * 3600) - (time_in_minutes * 60)

if time_in_hours < 1:  # определяем часы

    text_time_in_hours = "00"

# если время в часах больше 1, то определяем формат вывода чч
elif time_in_hours >= 9:

    text_time_in_hours = time_in_hours

else:

    text_time_in_hours = "0" + str(time_in_hours)

if time_in_minutes < 1:  # определяем минуты

    text_time_in_minutes = "00"

# если время в минутах больше 1, то определяем формат вывода мм
elif time_in_minutes >= 9:

    text_time_in_minutes = time_in_minutes

else:

    text_time_in_minutes = "0" + str(time_in_minutes)

# если время в секундах больше 1, то определяем формат вывода мм
if time_in_seconds >= 9:

    text_time_in_seconds = time_in_seconds

else:

    text_time_in_seconds = "0" + str(time_in_seconds)

print(f"{text_time_in_hours}.{text_time_in_minutes}.{text_time_in_seconds}")
