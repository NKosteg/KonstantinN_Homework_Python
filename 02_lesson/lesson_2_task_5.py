def month_to_season(month):
    if month == 12 or month == 1 or month == 2:
        return 'Зима'
    elif 3 <= month <= 5:
        return 'Весна'
    elif 6 <= month <= 8:
        return 'Лето'
    elif 9 <= month <= 11:
        return 'Осень'
    else:
        return 'Неверный номер месяца'

num_month = int(input('Введите номер месяца (1-12):'))
print(month_to_season(num_month))