#Код, вызывающий функцию с уже подставленным значением, и с использованием операций ветвления.
def is_year_leap(year):
    if year % 4 == 0:
        result = True
    else:
        result = False
    print('Год', year, ':', result)
is_year_leap(2021)

#Код, вызывающий функцию, при условии ввода года в консоль, и без использования операций ветвления.
def is_year_leap(year):
    result = year % 4 == 0
    return result
year = int(input('Введите год: '))
print(f'Високосный ли год {year}: {is_year_leap(year)}')

#Некоторая комбинация из двух вариантов, представленных выше
def is_year_leap(year):
    if year % 4 == 0:
        result = True
    else:
        result = False
    print('Високосный ли год', year, ':', result)
is_year_leap(int(input('Введите год: ')))

# P.S. Shadows name 'year' from outer scope - конфликт возникает из-за использования одноименной переменной во всех трех вариантах.
# Если оставить один вариант, код проходит проверку.
