import pytest
from calculator import Calculator



@pytest.fixture
def just_print_a_message():
    print('Начали выполнять тест')
    yield
    print("Закончили выполнять тест")

@pytest.fixture
def instance():
    return Calculator()