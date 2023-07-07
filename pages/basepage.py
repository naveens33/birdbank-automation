from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.__driver = driver

    def _click(self, locator):
        self.__driver.find_element(*locator).click()

    def _enter_text(self, locator, text):
        self.__driver.find_element(*locator).send_keys(text)

    def _wait_for_condition(self, locator, condition, timeout=5):
        wait = WebDriverWait(self.__driver, timeout)
        if condition == "visibility":
            return wait.until(EC.visibility_of_element_located(locator))
        elif condition == "invisibility":
            pass

    def _select_dropdown_by_text(self, locator, text):
        element = self.__driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def _get_text(self, locator):
        return self.__driver.find_element(*locator).text