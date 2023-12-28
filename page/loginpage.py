from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.lc = Locators()

    def enter_username(self, username):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.lc.txt_username_id))
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.lc.txt_password_id))
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.lc.login_button_xpath))
        ).click()

    def open_navigation_dropdown(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lc.Nav_totaloss_xpath))
        ).click()

    def click_open_option(self):
        # Assuming the Nav_Open_xpath represents the "Open" option
        open_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lc.Nav_Open_xpath))
        )
        open_option.click()
    def click_create_case(self):
        create_case = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lc.btncreatecase_xpath)))
        create_case.click()



    def select_Insurer(self):
        select_Insurer = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable("Insurer"))
        Select.select_by_index(2)


    # select.select_by_value("allianz")
    #select.select_by_index2

        assert "allianz" in select_Insurer.first_selected_option.text
        self.driver.quit()

    def enter_claim_number(self, claim_number):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.lc.txtClaimNumber_xpath))
        ).send_keys(claim_number)
        claim_number.clear()


    def enter_reg_number(self, reg_num):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.lc.txtRegNum_xpath))
        ).send_keys(reg_num)

    def drp_reg_state(self, reg_state):
        drpreg = Select(self.driver.find_element(By.XPATH, self.lc.drpInsurer_xpath))
        drpreg.select_by_visible_text(reg_state)

    def drp_assessment_party(self, assessment_party):
        drpassess = Select(self.driver.find_element(By.XPATH, self.lc.drpAssessParty_xpath))
        drpassess.select_by_visible_text(assessment_party)

    def drp_assessment_instruction(self, assessment_ins):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.ID, self.lc.drpAssessInstructions_xpath))
        ).send_keys(assessment_ins)
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()



