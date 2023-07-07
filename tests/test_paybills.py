import pytest

from pages.navigationbarpage import NavigationBarPage
from pages.paybillspage import PayBillsPage
from test_data.read_data import get_data


class Test_PayBills:

    @pytest.fixture(scope="class", autouse=True)
    def navigate_to_pay_bills(self, login, driver):
        navigation_bar = NavigationBarPage(driver)
        navigation_bar.click_pay_bills_link()

    @pytest.mark.parametrize("biller_name,registration_number, auto_pay", get_data("test_data/TestData.xls","AddNewBiller"))
    def test_add_new_biller(self, driver,biller_name,registration_number, auto_pay):
        paybills = PayBillsPage(driver)
        paybills.click_add_new_payee()
        paybills.do_add_new_biller(biller_name,registration_number, auto_pay)
        assert "Payee Added Successful" == paybills.get_confirmation_text(), \
            "Payment Confirmation message is not received"

    def test_pay_biller(self):
        pass
