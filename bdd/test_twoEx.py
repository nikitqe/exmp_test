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
    openSection = driver.find_element(By.XPATH, "//*[@itemprop='name' and text()='Строительные материалы']").get_attribute('innerHTML')
    assert openSection in section
    openCity = driver.find_element(By.XPATH, "//span[@data-test-id='CityName' and text()='Москва']").get_attribute('innerHTML')
    assert openCity in city


@when('в фильтре для <typeFilter> я выбираю <brand>')
def check_filter(driver, typeFilter, brand):
    driver.find_element(By.XPATH, "//button[text()='Бренд']")
    driver.find_element(By.XPATH, "(//span[@class='c151qo43'])[1]")


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
    openSection = driver.find_element(By.XPATH, "//*[@itemprop='name' and text()='Минеральная вата']").get_attribute('innerHTML')
    assert openSection in section
    openCity = driver.find_element(By.XPATH, "//span[@data-test-id='CityName' and text()='Москва']").get_attribute('innerHTML')
    assert openCity in city


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
    driver.find_element(By.XPATH, "//*[@class='tdc1jhj p6dine5']")


@then('я могу изменить количество')
def changeCounter(driver):
    driver.find_element(By.XPATH, "//button[@data-test-id='CounterUp']").click()  # добавить по кнопке + счетчитку
    driver.find_element(By.XPATH, "//button[@data-test-id='CounterUp']").click()
    driver.find_element(By.XPATH, "//button[@class='pp82xq9 bbw87z']").click()  # убрать товар по кнопке - счетчику
    changeNum = driver.find_element(By.XPATH, "//*[@class='t9v9037 s1lau469']")  # ввод числа с клавиатуры
    changeNum.click()
    changeNum.send_keys(Keys.CONTROL + "a")
    changeNum.send_keys("9")

# countMy = driver.find_elements(By.XPATH, "//*[@data-test-id='Product']")
# print (len(countMy))
# link = driver.find_element(By.XPATH, "//*[@data-test-id='LoadMoreButton']")
# link.click()
# time.sleep(1)
# newCount = driver.find_elements(By.XPATH, "//*[@data-test-id='Product']")
# print(len(newCount))
