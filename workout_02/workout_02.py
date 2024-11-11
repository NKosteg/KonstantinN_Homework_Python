# #1

employee_list = ["Jonh Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
print(employee_list[1],',',employee_list[-2])
print(employee_list[1] + ', ' + employee_list[-2])

# #2
# dev_by_three = input("Введите число:")
# num = int(dev_by_three)
# if num % 3 == 0:
#     print("Делится ли на три " + dev_by_three + " ? - Да")
# else:
#     print("Делится ли на три " + dev_by_three + " ? - Нет")
# #
# def dev_by_three(number):
#     return "Да" if number % 3 == 0 else "Нет"
#
# num = int(input("Введите число: "))
# result = dev_by_three(num)
# print(f"Делится ли на три {num}? - {result}")

# #3
# import math
# def min_boxes(number_of_items):
#     print(math.ceil(number_of_items / 5))
# number_of_items = int(input("Сколько предметов: "))
# min_boxes(number_of_items)
# #
# def min_boxes(number_of_items):
#     return math.ceil(number_of_items / 5)
# number_of_items = int(input("Сколько предметов: "))
# result = min_boxes(number_of_items)
# print(f"Минимальное количество коробок: {result}")
#
# import math
#
# def min_boxes(items):
#     return math.ceil(items / 5)
#
# num_items = int(input("Введите количество предметов: "))
# print(f"Минимальное количество коробок: {min_boxes(num_items)}")

## 4

# def check_divisibility(n):
#     for n in range(1,n + 1):
#         if n % 2 == 0 and n % 4 != 0:
#             print(str(n) + ' Делится на 2, но не на 4')
#         elif n % 2 == 0 and n % 4 == 0:
#             print(str(n) + ' Делится и на 2, и на 4')
#         else:
#             print(str(n))
#
# n = int(input('Введи число: '))
# check_divisibility(n)

# #5
# def quarter_of_year(month_num):
#     if month_num <1 or month_num >12:
#         return 'Неверный номер месяца'
#     elif month_num <= 3:
#         return 'I квартал'
#     elif month_num <= 6:
#         return 'II квартал'
#     elif month_num <= 9:
#         return 'III квартал'
#     else:
#         return 'IV квартал'
#
# month_num = int(input("Введите номер месяца: "))
# print(quarter_of_year(month_num))

##6
# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
# for n in lst:
#     if n > 15 and n % 3 == 0:
#         print(n)
##
# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
# result = [n for n in lst if  n > 15 and n %3 == 0]
# print(result)

# #7
# num_list = list(range(25, 0, -5))
# print(num_list)

# #8
# var_1 = 50
# var_2 = 5
##
# temp = var_1
# var_1 = var_2
# var_2 = temp
# #  или
# var_1, var_2 = var_2, var_1
##
# print("var_1 ", var_1)
# print("var_2 ", var_2)


