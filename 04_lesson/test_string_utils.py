import pytest
from string_utils import StringUtils

string_utils = StringUtils()

## string.capitilize()

@pytest.mark.parametrize('string, converted_string', [
    ('Skypro', 'Skypro'),                              # Сначала проверяем, что функция ничего не ломает
    ('skypro', 'Skypro'),                              # Проверяем, что возвращает первый символ в верхнем регисте
    ('SKYPRO', 'Skypro'),                              # Проверяем, что остальные символы возвращает в нижнем регистре
    ('upper LOWER', 'Upper lower')                     # Проверяем строку с пробелом
    ] )
def test_string_capitalize_positive(string, converted_string):
    result = string_utils.capitilize(string)
    assert result == converted_string

@pytest.mark.parametrize('string, converted_string',[
    ('1sKYPRO', '1skypro'),                            # При вводе не строкового символа вместо любого символа,
    ('sky4PRO', 'Sky4pro')                             # код возвращает его без изменений
    ] )                                                # остальные  символы обрабатывает, как и должен
def test_string_capitalize_int(string, converted_string):
    result = string_utils.capitilize(string)
    assert result == converted_string

@pytest.mark.xfail
def test_string_capitalize_emrty():
    result = string_utils.capitilize('')               # Пустая строка -> Здесь мы не знаем ожидаемый результат
    assert result == None

## string.trim(whitespace)

@pytest.mark.parametrize('siring, converted_string',[
    (' skypro', 'skypro'),                             # Проверка с одним пробелом перед текстом
    ('  skypro', 'skypro'),                            # Проверка с двумя пробелами перед текстом
    (' Yandex, Chrome', 'Yandex, Chrome')              # Проверка с пробелом как перед, так и внутри текста
    ] )
def test_string_removeprefix_positive(siring, converted_string):
    result = string_utils.trim(siring)
    assert result == converted_string

@pytest.mark.parametrize('siring', [
    (''),                                              # Проверка ввода пустой строки, возвращает пустую строку
    (' ')                                              # Проверка ввода строки с пробелами, возвращает пустую строку
    ] )
def test_string_removeprefix_negative(siring):
    result = string_utils.trim(siring)
    assert result == ''

## string.to_list

def test_string_to_list_defolt_delimeter():
    result = string_utils.to_list('a,b,c,d')              # Проверка с разделителем по умолчанию
    assert result == ['a','b','c','d']

@pytest.mark.parametrize('string, list_line, delimeter', [
    ('я:б:и:г', ['я','б','и','г'], ':'),                      # Две проверки с различными разделителями
    ('q/w/e/r/t/y', ['q','w','e','r','t','y'], '/'),          # с текстовыми символами
    ('1$2$3$4$5', ['1','2','3','4','5'], '$'),                # Проверка с нетекстовыми символами -> в строковый формат
    ('Test case&Check list',['Test case','Check list'], '&')    # Проверка, где строки с пробелом
    ] )
def test_string_to_list_positive(string, list_line, delimeter):
    result = string_utils.to_list(string, delimeter)
    assert result == list_line

@pytest.mark.parametrize('string', [
    (''),                                                 # Проверка пустой строки, возвращает пустой список
    ('  ')                                                # Проверка строки с пробелами, возвращает пустой список
    ])
def test_string_to_list_empty(string):
    result = string_utils.to_list(string)
    assert result == []

@pytest.mark.parametrize('string, list_line, delimeter', [
(' @ @ ', [' ',' ',' '], '@'),                            # Проверка строки с пробелами через разделитель
    ('^^', ['','',''],'^')                                # Проверка строки только с одними разделителями
    ] )
def test_string_to_list_negative(string, list_line, delimeter):
    result = string_utils.to_list(string,delimeter)
    assert result == list_line
    """" Поведение этой функции когда строка принимает такие значения, такое же как и с обычными символами:
    в первом случае выводится список со строками в которых только пробел и разделитель по умолчанию,
    во втором случае выводится список с пустыми строками, с разделителем по умолчанию.
    Технически это не считается ошибкой, поскольку список пустых строк, как и список строк с пробелами есть объект,
    но с практической стороны, такие объекты могут вызывать ошибки в дальнейшем. 
    ИМХО
    """

## string.contains

@pytest.mark.parametrize('string, symbol',[
    ('Yahoo', 'h'),                                       # Строка содержит искомый символ
    ('Портал', "П"),
    ('Google chrome', 'r'),                               # Строка с пробелом содержит искомый символ после пробела
    ('Google', '')                                        # Строка содержит искомый символ с пустым значением
    ] )
def test_string_index_positive(string, symbol):
    result = string_utils.contains(string, symbol)
    assert result == True

@pytest.mark.parametrize('string, symbol',[
    ('Yahoo', 'u'),                                       # Строка не содержит искомый символ
    ('Портал', "Я"),
    ('Google', ' ')
    ] )
def test_string_index_negative(string, symbol):
    result = string_utils.contains(string, symbol)
    assert result == False

def test_string_index_whitespase_empty():
    result = string_utils.contains(' ','')  # Строка -> пробел, искомый символ -> пустой
    assert result == True

def test_string_index_empty_whitespase():
    result = string_utils.contains('',' ')  # Строка -> пустая, искомый символ -> пробел
    assert result == False

## string.delete_symbol

@pytest.mark.parametrize('string, symbol, converted_string',[
    ('Yandex', 'd', 'Yanex'),                                 # В строке присутствует удаляемая подстрока
    ("Текст", "к", "Тест"),
    ("Тестирование", "ирование", "Тест"),
    ('SkyPro', 'Sky', 'Pro'),
    ('A string with spaces', 'with ', 'A string spaces'),     # В строке с пробелом присутствует удаляемая подстрока
    ('Goodle Chrome', ' ', 'GoodleChrome')                    # В строке с пробелом удаляемая подстрока -> пробел
    ] )
def test_string_replace_positive(string, symbol, converted_string):
    result = string_utils.delete_symbol(string, symbol)
    assert result == converted_string


@pytest.mark.parametrize('string, symbol, converted_string',[
    ('Yandex', 'i', 'Yandex',),                               # В строке отсутствует удаляемая подстрока
    ("Тестирование", "маска", "Тестирование")                 # Строка остается без изменений
    ] )
def test_string_replace_negative(string, symbol, converted_string):
    result = string_utils.delete_symbol(string, symbol)
    assert result == converted_string

@pytest.mark.parametrize('string, symbol, converted_string',[
    ('Yandex', 'D', 'Yandex'),                                # В строке есть удаляемый символ, но с другим регистром
    ("Текст", "Е", "Текст")                                   # Строка остается без изменений
    ] )
def test_string_replace_invalid_case(string, symbol, converted_string):
    result = string_utils.delete_symbol(string, symbol)
    assert result == converted_string

@pytest.mark.parametrize('string, symbol, converted_string', [
    ('Yandex', '', 'Yandex'),                                 # Значение удаляемой подстроки -> пустое или пробел
    ("Текст", " ", "Текст"),                                  # Строка остается без изменений
    ('','A', ''),                                             # В значении передается пустая строка
    (' ', 'B', ' ')                                           # В значении передается строка с пробелом
    ] )                                                       # Строка остается без изменений
def test_string_replace_empty(string, symbol, converted_string):
    result = string_utils.delete_symbol(string, symbol)
    assert result == converted_string

## string.starts_with

@pytest.mark.parametrize('string, symbol',[
    ('GoogleChrome', 'G'),                                    # Строка начинается с заданного символа
    ("ТестРан", "Т"),
    ('Yandex market', 'Y')                                    # Строка с пробелом начинается с заданного символа
    ] )
def test_string_startswith_positive(string, symbol):
    result = string_utils.starts_with(string, symbol)
    assert result == True

@pytest.mark.parametrize('string, symbol',[
    ('GoogleChrome', 'C'),                                    # Строка не начинается с заданного символа
    ("ТестРан", "Р"),
    ('Yandex', ' ')
    ] )
def test_string_startswith_negative(string, symbol):
    result = string_utils.starts_with(string, symbol)
    assert result == False

@pytest.mark.parametrize('string, symbol',[
    ('GoogleChrome', 'g'),                                    # Строка начинается с заданного символа,
    ('googleChrome', 'G'),                                    # но в другом регистре
    ("ТестРан", "т"),
    ("тестРан", "Т")
    ] )
def test_string_startswith_invalid_case(string, symbol):
    result = string_utils.starts_with(string, symbol)
    assert result == False

def test_string_startswith_symbol_empty():
    result = string_utils.starts_with('Yandex','')              # Символ -> пустой, отсутствует
    assert result == True

## string.end_swith

@pytest.mark.parametrize('string, symbol',[
    ('GoogleChrome', 'e'),                                    # Строка заканчивается заданным символом
    ("ТестРан", "н"),
    ('Yandex market', 't')                                    # Строка с пробелом заканчивается заданным символом
    ] )
def test_string_endswith_positive(string, symbol):
    result = string_utils.end_with(string, symbol)
    assert result == True

@pytest.mark.parametrize('string, symbol',[
    ('GoogleChrome', 'm'),                                    # Строка не заканчивается заданным символом
    ("ТестРан", "а"),
    ('Yandex', ' ')
    ] )
def test_string_endswith_negative(string, symbol):
    result = string_utils.end_with(string, symbol)
    assert result == False

@pytest.mark.parametrize('string, symbol',[
    ('GoogleChrome', 'E'),                                    # Строка заканчивается заданным символом,
    ('googleChromE', 'e'),                                    # но в другом регистре
    ("ТестРан", "Н"),
    ("тестРаН", "н")
    ])
def test_string_endswith_invalid_case(string, symbol):
    result = string_utils.end_with(string, symbol)
    assert result == False

def test_string_endswith_symbol_empty():
    result = string_utils.end_with('Yandex','')  # Символ -> пустой, отсутствует
    assert result == True

## string.is_empty

@pytest.mark.parametrize('string', [
    (''),                                                      # Пустая строка
    ('  ')                                                     # Строка с пробелами
    ] )
def test_string_is_empty_positive(string):
    result = string_utils.is_empty(string)
    assert result == True

@pytest.mark.parametrize('string', [
    ('Yandex'),                                                # Строка с латинскими символами
    ('Тест Ран'),                                              # Строка с символами кириллицы
    ('12345')                                                  # Строка с не текстовыми символами
    ] )
def test_string_is_empty_negative(string):
    result = string_utils.is_empty(string)
    assert result == False

## string.list_to_string

def test_list_to_string_defolt_joiner():
    result = string_utils.list_to_string(['a','b','c','d'])    # Проверка с разделителем по умолчанию
    assert result == 'a, b, c, d'

@pytest.mark.parametrize('list_line, converted_string, joiner', [
    ([1,2,3,4], '1:2:3:4', ':'),                               # Значения в числовом формате -> в строковый формат
    (['Test','case'], 'Test-case', '-'),                       # Две проверки с различными разделителями
    (["Выполнен", "Провален"], "Выполнен/Провален", "/"),      # с текстовыми символами
    (['Test case', 'Check list'], 'Test case&Check list', '&')   # Проверка значений с пробелом
    ] )
def test_list_to_string_positive(list_line, converted_string, joiner):
    result = string_utils.list_to_string(list_line, joiner)
    assert result == converted_string

@pytest.mark.parametrize('list_line', [
    ([]),                                                      # Проверка пустого списка, возвращает пустую строку
    ([  ])                                                     # Проверка списка с пробелами, возвращает пустую строку
    ])
def test_list_to_string_negative(list_line):
    result = string_utils.list_to_string(list_line)
    assert result == ''



