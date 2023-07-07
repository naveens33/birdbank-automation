from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class PayBillsPage(BasePage):
    __add_payee_button = By.ID, "add_payee"
    __biller_name_field = By.XPATH, '//input[@placeholder="Enter Biller Name"]'
    __registration_number_field = By.XPATH, '//input[@placeholder="Enter Registration Number"]'
    __auto_pay_radio_no = By.XPATH, '//label[@for="no"]'
    __auto_pay_radio_yes = By.XPATH, '//label[@for="yes"]'
    __pay_limit_field = By.XPATH, '//input[@placeholder="Enter Pay Limit"]'
    __frequency_dropdown = By.ID, "frequency"
    __save_button = By.ID, "save"
    __confirmation_text = By.ID, "confirmationMessage"

    def click_add_new_payee(self):
        self._click(self.__add_payee_button)

    def do_add_new_biller(self, biller_name, registration_number, auto_pay="no",
                          pay_limit=None, pay_frequency=None, pay_start_date=None, pay_end_date=None):
        self._wait_for_condition(self.__biller_name_field,"visibility").send_keys(biller_name)
        self._enter_text(self.__registration_number_field,registration_number)
        if auto_pay == "no":
            self._click(self.__auto_pay_radio_no)
        else:
            self._click(self.__auto_pay_radio_yes)
            self._enter_text(self.__pay_limit_field,pay_limit)
            self._select_dropdown_by_text(self.__frequency_dropdown,pay_frequency)

        self._click(self.__save_button)

    def get_confirmation_text(self):
        return self._get_text(self.__confirmation_text)


