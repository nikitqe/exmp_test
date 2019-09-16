from pytest_bdd import scenario
from bdd.test_twoEx import *


@scenario('twoEx.feature',
          'Проверка товара с ценой от',
          example_converters=dict(city=str, section=str, typeFilter=str, brand=str)
          )
def test_check_tovar():
    pass


@scenario('twoEx.feature',
          'Кладем товар в корзину',
          example_converters=dict(city=str, section=str, count=str, miscure=str)
          )
def test_add_tovar():
    pass
