import pytest
from calculator import Calculator


@pytest.mark.positive_test
@pytest.mark.parametrize(
    'nums, result',
    [
        ([], 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5)
    ]
)
def test_avg_list(nums, result, just_print_a_message, instance: Calculator):
    assert instance.avg(nums) == result