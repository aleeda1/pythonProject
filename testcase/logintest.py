import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.core import driver
from webdriver_manager.chrome import ChromeDriverManager
from locators.locators import Locators
from page.loginpage import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://cepuat.controlexpert.expert/Identity/Account/Login?ReturnUrl=%2F")

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("aaditya@claimstrak.co.uk", "Cepuat2023#")

        login_page.open_navigation_dropdown()
        login_page.click_open_option()
        login_page.click_create_case()


        # select.select_by_value("allianz")
        # select.select_by_index(2)

        assert "allianz" in select.first_selected_option.text
        self.driver.quit()


    # def test_Insurer(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.select_Insurer('Allianz')
    #     selected_insurer = login_page.get_selected_insurer()
    #     self.assertEqual(selected_insurer, 'Allianz', "Selected insurer doesnt match ")
    #     time.sleep(10)

        # login_page = LoginPage(self.driver)
        # time.sleep(10)
        # login_page.enter_claim_number("123456")

        # login_page.enter_reg_number()

       # WebDriverWait(driver, 10).until(
         #   EC.element_to_be_clickable((By.ID, 'your_dropdown_id'))
      #  )


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
