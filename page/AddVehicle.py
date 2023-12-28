from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.Case import CreateCase
from selenium import webdriver

class Case:
    def __init__(self, driver):
        self.driver = driver
        self.locators = CreateCase()

    def open_insurance_form(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.locators.btncreatecase_xpath))).click()

    def select_insurer(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.locators.drpInsurer_xpath))
        drp.select_by_visible_text(value)

    def enter_claim_number(self, claim_number):
        """Enter the claim number into the corresponding text field."""
        self.driver.find_element(By.XPATH, self.locators.txtClaimNumber_xpath).send_keys(claim_number)

    def select_policy_type(self, policy_type):
        """Select the policy type from the dropdown."""
        drp = Select(self.driver.find_element(By.XPATH, self.locators.drpPolicyType_xpath))
        drp.select_by_visible_text(policy_type)

    def enter_risk_description(self, risk_description):
        """Enter the risk description into the corresponding text field."""
        self.driver.find_element(By.XPATH, self.locators.txtRisk_xpath).send_keys(risk_description)

# Example of using the Case class in a test
if __name__ == '__main__':
    # Initialize the webdriver
    driver = webdriver.Chrome()

    # Create an instance of the Case class
    case_instance = Case(driver)

    # Specify the URL for opening the insurance form
    insurance_form_url = "https://cepuat.controlexpert.expert/TotalLoss/CreateTotalLossCase/5ae9ed17-1828-40bd-9eeb-321247a8527f"

    # Use methods from the Case class
    case_instance.open_insurance_form(insurance_form_url)
    case_instance.select_insurer('ABC Insurance')
    case_instance.enter_claim_number('123456')
    case_instance.select_policy_type('Full Coverage')
    case_instance.enter_risk_description('Accident prone area')

    # Close the webdriver
    driver.quit()
