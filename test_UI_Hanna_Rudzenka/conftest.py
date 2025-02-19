import pytest
from faker import Faker
from random import randint
from test_UI_Hanna_Rudzenka.pages.create_account_page import CreateAccount
from test_UI_Hanna_Rudzenka.pages.sale_page import SalePage
from test_UI_Hanna_Rudzenka.pages.eco_friendly_page import EcoFriendly
from test_UI_Hanna_Rudzenka.pages.customer_account_page import CustomerAccount


@pytest.fixture()
def sale(page):
    return SalePage(page)


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendly(page)


@pytest.fixture()
def create_account(page):
    return CreateAccount(page)


@pytest.fixture()
def customer_account(page):
    return CustomerAccount(page)


@pytest.fixture()
def create_test_data():
    faker_data = Faker()
    password = faker_data.password(length=randint(8, 15), digits=True, upper_case=True, lower_case=True,
                                   special_chars=True)
    return {
        'name': faker_data.name(),
        'last_name': faker_data.last_name(),
        'email': faker_data.email(),
        'password': password,
        'password_confirm': password
    }
