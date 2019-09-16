import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    b = webdriver.Chrome()
    b.implicitly_wait(5)
    yield b
    b.quit()
