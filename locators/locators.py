from selenium.webdriver.common.by import By
class Locators:
    txt_username_id = "Input_Email"
    txt_password_id = "Input_Password"
    login_button_xpath = "//button[contains(text(),'Login')]"
    Nav_totaloss_xpath = "//body/div[1]/aside[1]/div[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]"
    Nav_Open_xpath = "//body/div[1]/aside[1]/div[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]"
    btncreatecase_xpath = "//input[@id='btn-CreateTotalLossCase']"
    drpInsurer_xpath = "//select[@id='Insurer']"
    txtClaimNumber_xpath = "//input[@id='ClaimInfo_Number']"
    txtRegNum_xpath = "//input[@id='RegistrationNumber']"
    drpRegState_xpath = "//select[@id='RegistrationState']"
    drpAssessParty_xpath = "//select[@id='AssessmentParty']"
    drpAssessInstructions_xpath = "//select[@id='AssessmentInstruction']"

