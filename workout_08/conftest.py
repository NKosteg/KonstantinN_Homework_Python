import pytest

from CompanyApi import CompanyApi

@pytest.fixture(scope="session")
def client():
    return CompanyApi('http://5.101.50.27:8000')

# @pytest.fixture(autouse=True) # Для автовыполнения во всех тестах
# def my_fix():
#     pass