import pytest
from calculator import Calculator


@pytest.mark.positive_test
def test_div_positive(just_print_a_message, instance: Calculator):
    assert instance.div(10, 2)

def test_div_by_zero(just_print_a_message, instance: Calculator):
    with pytest.raises(ArithmeticError):
        instance.div(10, 0)