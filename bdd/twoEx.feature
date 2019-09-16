# coding=utf-8
Scenario Outline: Проверка товара с ценой от
    Given открыта листинга товаров <section>, города <city>
    When в фильтре для <typeFilter> я выбираю <brand>
    Then первый товар имеет кнопку Подробнее

    Examples: Vertical
    | city       | Москва                 |
    | section    | Строительные материалы |
    | typeFilter | Бренд                  |
    | brand      | Knauf                |


Scenario Outline: Кладем товар в корзину
    Given открыта страница листинга товаров <section>, города <city>
    And первый товар на странице
    When кликаю по кнопке В корзину
    Then текст кнопки меняется на В корзине <count> <measure>
    And я вижу счетчик
    And я могу изменить количество

    Examples: Vertical
    | city       | Москва                 |
    | section    | Минеральная вата       |
    | count      | 1                      |
    | measure    | уп                     |