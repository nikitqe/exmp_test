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


Scenario Outline: Проверка постраничной навигации
    Given открыта страница листинга товаров <section1>, города <city>
    When есть блок постраничной навигации и кнопка Показать еще
    Then я могу переходить по ссылкам страниц
    And я вижу 60 товаров
    And кликаю на Показать еще
    And я вижу 120 товара
    And кликаю по ссылке страницы <page>

    Examples: Vertical
    | city        | Москва                   |
    | section1    | Строительные материалы   |
    | page        | 2                        |


Scenario Outline: Проверка disabled фильтров
    Given открыта страница листинга товаров <section>, города <city>
    When в фильтре для <typeFilter> я выбираю <brand>
    Then в фильтре для <typeFilter2> проверяю, что есть [type=checkbox]:disabled
    And в фильтре для <typeFilter> я снимаю выбор <brand>
    And в фильтре для <typeFilter2> проверяю, что нет [type=checkbox]:disabled
    And в фильтре для <typeFilter> я выбираю <brand>
    And я выбираю случайно любую категорию в <typeFilter3>
    And во всех фильтрах проверяю, что нет [type=checkbox]:disabled



    Examples: Vertical
    | city         | Москва                                                              |
    | section      | Минеральная вата                                                    |
    | typeFilter   | Бренд                                                               |
    | brand        | Rockwool                                                            |
    | typeFilter2  | Плотность                                                           |
    | typeFilter3  | Категории                                                           |