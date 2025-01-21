import pytest
from calculator import Calculator


@pytest.mark.positive_test
@pytest.mark.parametrize(
    'num1, num2, result',
    [
        (4, 5, 9),
        (-6, -10, -16),
        (-6, 6, 0),
        (5.61, 4.29, 9.9),
        (10, 0, 10),
        (-10.5, 1234, 1223.5)
    ]
)
def test_sum_nums(just_print_a_message, num1, num2, result, instance: Calculator):
    assert instance.sum(num1, num2) == result




