import pytest
from string_processor import StringProcessor

string_processor = StringProcessor()

@pytest.mark.parametrize('string, valid_string', [
    ('Verification text', 'Verification text.'),
    ('verification text.', 'Verification text.'),
    ('verification text', 'Verification text.')])
def test_process_positive1(string, valid_string):
    res = string_processor.process(string)
    assert res == 'Verification text.'

def test_process_empty():
    res = string_processor.process('')
    assert res == '.'

def test_process_whitespace():
    res = string_processor.process(' ')
    assert res == '.'

def test_process_number():
    with pytest.raises(TypeError):
        string_processor.process(1234)


# def test_process_positive2():
#     res = string_processor.process('verification text.')
#     assert res == 'Verification text.'
# def test_process_positive3():
#     res = string_processor.process('Verification text')
#     assert res == 'Verification text.'
#
# def test_process_negative1():
#     res = string_processor.process(12345)
#     assert res == 'Verification text.'
#
# def test_process_negative2():
#     res = string_processor.process('')
#     assert res == 'Verification text.'
#
# def test_process_negative3():
#     res = string_processor.process('  ')
#     assert res == 'Verification text.'


# res = string_processor.process('Verification text.')
# print(res)
# assert res == 'Verification text.'
#
# res = string_processor.process('Verification text')
# print(res)
# assert res == 'Verification text.'
#
# res = string_processor.process('verification text.')
# print(res)
# assert res == 'Verification text.'