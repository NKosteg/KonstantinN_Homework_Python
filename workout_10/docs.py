# int - 15
# float - 2,6
# bool - True/False
# str -'Test'
# dict - {}
# list - []
# <class> - Card(как пример обозначения класса, здесь его нет)

def do_it(param_1 : int, param_2 : int, param_3 : float) -> list:
    """
    Функция берет первые два параметра, складывает их и делит на третий
    результат выводит в консоль
    параметры должны быть числовыми
    """
    result = (param_1 + param_2) * param_3
    return [param_1, param_2, param_3, result]

do_it(1, 2, 3.6)

