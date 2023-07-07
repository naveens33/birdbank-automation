pages -> Page Classes which consist of page objects and page actions
         BasePage class which consist of all the selenium interactions 
                def click(locator):
                        driver.find_element(locator).click()
                def enter_text(locator, text):
                        driver.find_element(locator).send_keys(text)
                
        Example: 
            class HomePage(BasePage):
                login_button = (id, "signin_button")

                def click_login_button(self):
                        # code to click the login button
                        self.click(login_button)
                
        
test_data -> read_data.py -> get_data(filename, sheetname) -> return the testdata in list of list 
                test_data.xls
 
reports (directory) -> html report stored here. also logger files 

tests -> all our pytest files will be maintained here 
        Example:
                test_pay_bills.py 
                        class AddNewBiller:
                                pass
                        
                        class PayBills:
                                pass

confttest.py -> all our fixtures which is used across the test files are maintained 

pytest.ini -> all our test configurations are maintained in this file
