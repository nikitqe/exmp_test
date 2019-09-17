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


@scenario('twoEx.feature',
          'Проверка постраничной навигации',
          example_converters=dict(city=str, section1=str, page=str)
          )
def test_navi_page():
    pass


@scenario('twoEx.feature',
          'Проверка disabled фильтров',
          example_converters=dict(city=str, section=str, typeFilter=str, brand=str, typeFilter2=str, typeFilter3=str)
          )
def test_dis_filter():
    pass
