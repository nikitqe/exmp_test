from pytest_bdd import scenario, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

stroi_mat = 'https://www.sdvor.com/moscow/catalog/stroitelnye-materialy-5521/'
min_vata = 'https://www.sdvor.com/moscow/catalog/mineralnaja-vata-5532/'


# Scenario Outline: Проверка товара с ценой от


@given('открыта листинга товаров <section>, города <city>')
def open_list_city(driver, section, city):
    driver.get(stroi_mat)
    open_katalog = driver.find_element(By.XPATH,"//*[@itemprop='name' and text()='Строительные материалы']").get_attribute('innerHTML')
    assert open_katalog in section
    open_city = driver.find_element(By.XPATH, "//span[@data-test-id='CityName' and text()='Москва']").get_attribute('innerHTML')
    assert open_city in city


@when('в фильтре для <typeFilter> я выбираю <brand>')
def check_filter(driver, typeFilter, brand):
    driver.find_element(By.XPATH, "//button[text()='Бренд']")
    driver.find_element(By.XPATH, "(//*[@role='checkbox'])[1]")

# "//*[@data-test-id='Filters']/div[2]/div/button")

@then('первый товар имеет кнопку Подробнее')
def first_more_detail(driver):
    button_more = driver.find_element(By.XPATH, "(//*[@data-test-id='Product']//span)[2]").get_attribute('innerHTML')
    print(button_more )
    assert button_more  in 'Подробнее'


# Scenario Outline: Кладем товар в корзину


@given('открыта страница листинга товаров <section>, города <city>')
def step_impl(driver, section, city):
    driver.get(min_vata)
    open_katalog = driver.find_element(By.XPATH, "//*[@itemprop='name' and text()='Минеральная вата']").get_attribute('innerHTML')
    assert open_katalog in section
    open_city = driver.find_element(By.XPATH, "//span[@data-test-id='CityName' and text()='Москва']").get_attribute('innerHTML')
    assert open_city in city


@given('первый товар на странице')
def first_product_on_page(driver):
    driver.find_element(By.XPATH, "(//*[@data-test-id='Product'])[1]")


@when('кликаю по кнопке В корзину')
def add_product(driver):
    driver.find_element(By.XPATH, "(//button[@data-test-id='AddButton'])[1]").click()  # добавить товар в корзину


@then('текст кнопки меняется на В корзине <count> <measure>')
def rename_button(driver, count, measure):
    to_basket = driver.find_element(By.XPATH, "(//*[@data-test-id='QuantityInCart'])[1]")
    put_busket = to_basket.get_attribute('innerHTML')
    print("В корзине" + " " + count + " " + measure)
    assert put_busket in 'В корзине 1 уп'


@then('я вижу счетчик')
def lookCounterUp(driver):
    driver.find_element(By.XPATH, "//*[@type='number']")


@then('я могу изменить количество')
def changeCounter(driver):
    driver.find_element(By.XPATH, "//button[@data-test-id='CounterUp']").click()  # добавить по кнопке + счетчитку
    driver.find_element(By.XPATH, "//button[@data-test-id='CounterUp']").click()
    driver.find_element(By.XPATH, "//div[button[@data-test-id='CounterUp']]/button[1]").click()  # убрать товар по кнопке - счетчику
    change_num = driver.find_element(By.XPATH, "//label[span[input[@type='number']]]")  # ввод числа с клавиатуры
    change_num.click()
    change_num.send_keys(Keys.CONTROL + "a")
    change_num.send_keys("9")


# Scenario Проверка постраничной навигации


@given('открыта страница листинга товаров <section1>, города <city>')
def firstpage(driver, section1, city):
    driver.get(stroi_mat)
    open_katalog = driver.find_element(By.XPATH,"//*[@itemprop='name' and text()='Строительные материалы']").get_attribute('innerHTML')
    assert open_katalog in section1
    open_city = driver.find_element(By.XPATH, "//span[@data-test-id='CityName' and text()='Москва']").get_attribute('innerHTML')
    assert open_city in city


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
    count_product = driver.find_elements(By.XPATH, "//*[@data-test-id='Product']")
    print(len(count_product))


@then('кликаю на Показать еще')
def clickMore_button(driver):
    button_more = driver.find_element(By.XPATH, "//*[@data-test-id='LoadMoreButton']")
    button_more.click()
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

#Scenatio DISABLE FILTER

@given('открыта страница листинга товаров <section>, города <city>')
def open_page_min_vata(driver, section, city):
    driver.get(min_vata)
    open_katalog = driver.find_element(By.XPATH, "//*[@itemprop='name' and text()='Минеральная вата']").get_attribute('innerHTML')
    assert open_katalog in section
    open_city = driver.find_element(By.XPATH, "//span[@data-test-id='CityName' and text()='Москва']").get_attribute('innerHTML')
    assert open_city in city

@when('в фильтре для <typeFilter> я выбираю <brand>')
def open_filter_brand(driver, typeFilter, brand):
    driver.find_element(By.XPATH, "//label[input[@name='brands' and @value='Rockwool']]")
    driver.find_element(By.XPATH, "(//*[@role='checkbox'])[1]").click()

@then('в фильтре для <typeFilter2> проверяю, что есть [type=checkbox]:disabled')
def check_is_disabled(driver, typeFilter2):
    driver.find_element(By.XPATH, "((//*[@data-test-id='FiltersOption'])[4]//div/button/span)[1]").click()
    checkdisabled = driver.find_element(By.XPATH, "(//*[@data-test-id='FiltersOption'])[4]//div/div/label/input").get_attribute("disabled")
    print('atribut in check_is_disabled:',checkdisabled)

@then('в фильтре для <typeFilter> я снимаю выбор <brand>')
def unchecked_filter_brand(driver, typeFilter, brand):
    time.sleep(3)
    move_button = driver.find_element(By.XPATH, "//*[@data-test-id='Filters']/div[2]/div/button")
    action = ActionChains(driver)
    action.move_to_element(move_button).perform()
    driver.find_element(By.XPATH, "//label[input[@name='brands' and @value='Rockwool']]")
    driver.find_element(By.XPATH, "(//*[@role='checkbox'])[1]").click()

@then('в фильтре для <typeFilter2> проверяю, что нет [type=checkbox]:disabled')
def check_non_disabled(driver, typeFilter2):
    time.sleep(1)
    checkingfilter_two = driver.find_element(By.XPATH, "(//*[@data-test-id='FiltersOption'])[4]//div/div/label/input").get_attribute("disabled")
    print('atribut in check_non_disabled:', checkingfilter_two)

@then('в фильтре для <typeFilter> я выбираю <brand>')
def again_unchecked_filter(driver, typeFilter, brand):
    driver.find_element(By.XPATH, "//label[input[@name='brands' and @value='Rockwool']]")
    driver.find_element(By.XPATH, "(//*[@role='checkbox'])[1]").click()
    driver.execute_script("document.activeElement.blur();")


@then('я выбираю случайно любую категорию в <typeFilter3>')
def random_filter(driver, typeFilter3):
    asd1 = driver.find_element_by_xpath("//*[@data-test-id='Filters']/div[1]")
    action = ActionChains(driver)
    action.move_to_element(asd1).perform()
    driver.find_element_by_link_text('Экструдированный пенополистирол (XPS)').click()
    time.sleep(1)
    cur_url = driver.current_url
    print(cur_url)

@then('во всех фильтрах проверяю, что нет [type=checkbox]:disabled')
def all_filter_unchecked(driver):
    time.sleep(1)
    checkingfilter_all = driver.find_element(By.XPATH, "//*[@type='checkbox']").get_attribute("disabled")
    print('all_filter_unchecked:', checkingfilter_all)

