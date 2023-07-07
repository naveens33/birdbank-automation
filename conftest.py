import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.homepage import HomePage
from pages.loginpage import LoginPage


@pytest.fixture(scope="session", autouse=True)
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    driver_ = webdriver.Chrome(options=options)
    driver_.maximize_window()
    driver_.get("https://birdbank.pythonanywhere.com/")

    return driver_


@pytest.fixture(scope="module")
def login(driver):
    home = HomePage(driver)
    home.click_login_button()
    login = LoginPage(driver)
    login.do_login("testuser1","testpassword")
