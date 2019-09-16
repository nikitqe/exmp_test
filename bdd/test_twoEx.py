from pytest_bdd import scenario, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

stroi_mat = 'https://www.sdvor.com/moscow/catalog/stroitelnye-materialy-5521/'
min_vata = 'https://www.sdvor.com/moscow/catalog/mineralnaja-vata-5532/'


# Scenario Outline: Проверка товара с ценой от


@given('открыта листинга товаров <section>, города <city>')
def open_list_city(driver, section, city):
    driver.get(stroi_mat)
    openSection = driver.find_element(By.XPATH,"//*[@itemprop='name' and text()='Строительные материалы']").get_attribute('innerHTML')
    assert openSection in section
    openCity = driver.find_element(By.XPATH, "//span[@data-test-id='CityName' and text()='Москва']").get_attribute('innerHTML')
    assert openCity in city


@when('в фильтре для <typeFilter> я выбираю <brand>')
def check_filter(driver, typeFilter, brand):
    driver.find_element(By.XPATH, "//button[text()='Бренд']")
    driver.find_element(By.XPATH, "(//*[@role='checkbox'])[1]")

# "//*[@data-test-id='Filters']/div[2]/div/button")

@then('первый товар имеет кнопку Подробнее')
def first_more_detail(driver):
    moreDetail = driver.find_element(By.XPATH, "(//*[@data-test-id='Product']//span)[2]").get_attribute('innerHTML')
    print(moreDetail)
    assert moreDetail in 'Подробнее'


# Scenario Outline: Кладем товар в корзину


@given('открыта страница листинга товаров <section>, города <city>')
def step_impl(driver, section, city):
    driver.get(min_vata)
    openNew = driver.find_element(By.XPATH, "//*[@itemprop='name' and text()='Минеральная вата']").get_attribute('innerHTML')
    assert openNew in section
    openNewCity = driver.find_element(By.XPATH, "//span[@data-test-id='CityName' and text()='Москва']").get_attribute('innerHTML')
    assert openNewCity in city


@given('первый товар на странице')
def first_product_on_page(driver):
    driver.find_element(By.XPATH, "(//*[@data-test-id='Product'])[1]")


@when('кликаю по кнопке В корзину')
def add_product(driver):
    driver.find_element(By.XPATH, "(//button[@data-test-id='AddButton'])[1]").click()  # добавить товар в корзину


@then('текст кнопки меняется на В корзине <count> <measure>')
def rename_button(driver, count, measure):
    toBasket = driver.find_element(By.XPATH, "(//*[@data-test-id='QuantityInCart'])[1]")
    putBusket = toBasket.get_attribute('innerHTML')
    print("В корзине" + " " + count + " " + measure)
    assert putBusket in 'В корзине 1 уп'


@then('я вижу счетчик')
def lookCounterUp(driver):
    driver.find_element(By.XPATH, "//*[@type='number']")


@then('я могу изменить количество')
def changeCounter(driver):
    driver.find_element(By.XPATH, "//button[@data-test-id='CounterUp']").click()  # добавить по кнопке + счетчитку
    driver.find_element(By.XPATH, "//button[@data-test-id='CounterUp']").click()
    driver.find_element(By.XPATH, "//div[button[@data-test-id='CounterUp']]/button[1]").click()  # убрать товар по кнопке - счетчику
    changeNum = driver.find_element(By.XPATH, "//label[span[input[@type='number']]]")  # ввод числа с клавиатуры
    changeNum.click()
    changeNum.send_keys(Keys.CONTROL + "a")
    changeNum.send_keys("9")


# Scenario Проверка постраничной навигации


@given('открыта страница листинга товаров <section1>, города <city>')
def firstpage(driver, section1, city):
    driver.get(stroi_mat)
    openOldSection = driver.find_element(By.XPATH,"//*[@itemprop='name' and text()='Строительные материалы']").get_attribute('innerHTML')
    assert openOldSection in section1
    openOldCity = driver.find_element(By.XPATH, "//span[@data-test-id='CityName' and text()='Москва']").get_attribute('innerHTML')
    assert openOldCity in city


@when('есть блок постраничной навигации и кнопка Показать еще')
def naviBlok_MoreDetail(driver):
    driver.find_element(By.XPATH, "//*[@data-test-id='Pagination']/ul[1]")
    driver.find_element(By.XPATH, "//*[@data-test-id='LoadMoreButton']")


@then('я могу переходить по ссылкам страниц')
def change_page(driver):
    driver.find_element(By.XPATH, "//*[@href='/moscow/catalog/stroitelnye-materialy-5521/']")
    next_page = driver.find_element_by_link_text('2')
    next_page.click()


@then('я вижу 60 товаров')
def look_60_product(driver):
    countMy = driver.find_elements(By.XPATH, "//*[@data-test-id='Product']")
    print(len(countMy))


@then('кликаю на Показать еще')
def clickMore_button(driver):
    moreButton = driver.find_element(By.XPATH, "//*[@data-test-id='LoadMoreButton']")
    moreButton.click()
    time.sleep(1)


@then('я вижу 120 товара')
def look_120_product(driver):
    newCount = driver.find_elements(By.XPATH, "//*[@data-test-id='Product']")
    print(len(newCount))


@then('кликаю по ссылке страницы <page>')
def clickOn_page(driver, page):
    link_page = driver.find_element_by_link_text(page)
    link_page.click()
    time.sleep(1)
    url = driver.current_url
    print(url)
