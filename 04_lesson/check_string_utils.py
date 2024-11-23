import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# res = string_utils.capitilize('sKYPRO  ')
# print(res)
# assert res == 'Skypro'
#
# def capitilize(string):
#     return string.capitalize()
# text = input('Enter text: ')
# print(capitilize(text))


# def trim(string):
#     whitespace = " "
#     while string.startswith(whitespace):
#         string = string.removeprefix(whitespace)
#     return string
# text = input('Enter text: ')
# print(trim(text))


def to_list(string, delimeter=","):
    if string.is_empty():
        return []
    return string.split(delimeter)
text = input('Enter text: ')
d = input('Enter delimeter: ')
print(to_list(text, d))

#
# string = "python is AWesome."
# capitalized_string = string.capitalize()
# print('Old String: ', string)
# print('Capitalized String:', capitalized_string)
# # Источник: https://pythonstart.ru/string/capitalize-python

