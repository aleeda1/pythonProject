import unittest
from selenium import webdriver
from page.AddVehicle import Case

class TestCaseForInsuranceForm(unittest.TestCase):
    def setUp(self):
        # Initialize WebDriver and Case instance before each test
        self.driver = webdriver.Chrome()
        self.case = Case(self.driver)

    def test_open_insurance_form(self):
        # Open the insurance form using the provided URL
        url = "https://cepuat.controlexpert.expert/TotalLoss/CreateTotalLossCase/5ae9ed17-1828-40bd-9eeb-321247a8527f"
        self.case.open_insurance_form(url)

    def test_fill_insurance_form(self):
        data_list = [
            {'drpInsurer_xpath': 'ABC Insurance', 'claim_number': '123456', 'registration_number': 'ABC123',
             'assessment_party': 'Assessor', 'assessment_instruction': 'Standard Inspection',
             'policy_number': 'POL123', 'vehicle_type': 'Sedan', 'value_cover': 'Comprehensive',
             'agreed_value': '50000', 'policy_type': 'Full Coverage', 'risk_description': 'Accident prone area'},
        ]

        for data in data_list:
            # Fill the insurance form using the test data
            self.case.locators.select_insurer(data['drpInsurer_xpath'])
            self.case.locators.txtClaimNumber_xpath(data['claim_number'])
            self.case.locators.txtRegNum_xpath(data['registration_number'])
            self.case.locators.drpRegState_xpath(data['Registration State'])
            self.case.locators.drpAssessParty_xpath(data['assessment_party'])
            self.case.locators.drpAssessInstructions_xpath(data['assessment_instruction'])
            self.case.locators.txtVehicleSupplierName_xpath(data['policy_number'])


            # Assertion to check if the submission is successful
            self.assertTrue(self.case.is_submission_successful())

    def tearDown(self):
        # Perform cleanup after each test
        print(type(self.driver))
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
