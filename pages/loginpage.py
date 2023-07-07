from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class LoginPage(BasePage):
    __username = By.NAME, "username"
    __password = By.ID, "id_password"
    __login_button = By.ID, "signin"

    def do_login(self, username, password):
        self._enter_text(self.__username, username)
        self._enter_text(self.__password, password)
        self._click(self.__login_button)