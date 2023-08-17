from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


class Login:

    textbox_accessCode_key = "123123123"
    textbox_accessCode_name = '//input[contains(@class, "slds-input") and contains(@name,"accessCode")]'
    textbox_username_id = "UserName"
    textbox_password_id = "Password"
    button_acknowledge_xpath = '//button[contains(@class, "slds-button slds-button_brand") and contains(text(), "Acknowledge")]'
    button_validateCode_name = '//button[contains(@class, "slds-button slds-button_brand") and contains(text(), "Validate Code")]'
    button_getStarted_name = '//button[contains(@class, "slds-button slds-button_brand") and contains(text(), "Get Started")]'
    button_AccountSubmit_name = '//button[contains(@class, "slds-button slds-button_brand") and contains(text(), "Submit")]'
    textbox_FirstName_Value = "Pat"
    textbox_LastName_Value = "Doe181293090"
    textBox_DOB_Value = "01/01/1960"
    textbox_SSN_Value = "3090"
    textbox_zip_Value = "08234"
    textbox_FirstName_Class = '//lightning-input[contains(@class, "fName")]//div[1]//div[1]//input[contains(@class, "slds-input")]'
    textbox_LastName_Class = '//lightning-input[contains(@class, "lName")]//div[1]//div[1]//input[contains(@class, "slds-input")]'
    textBox_DOB_Class = '//lightning-input[contains(@class, "dobPicker")]//lightning-datepicker[1]//div[1]//div[1]//input[contains(@class, "slds-input")]'
    textbox_SSN_Class = '//lightning-input[contains(@class, "ssn")]//div[1]//div[1]//input[contains(@class, "slds-input")]'
    textbox_SSNRecheck_Class = '//lightning-input[contains(@class, "verifySSN ")]//div[1]//div[1]//input[contains(@class, "slds-input")]'
    textbox_zip_Class = '//lightning-input[contains(@class, "zip")]//div[1]//div[1]//input[contains(@class, "slds-input")]'
    link_logout_linktest = "Logout"
    button_acknowledge_xpath1 = ''

    def __init__(self, driver):
        self.driver = driver

    def clickAcknowledgement(self):
        self.driver.find_elements(By.XPATH, self.button_acknowledge_xpath).click()

    def clickAcknowledgementSelector(self):
        self.driver.find_element(By.XPATH, self.button_acknowledge_xpath).click()

    def setpasscode(self, passcode):
        self.driver.find_element(By.XPATH, self.textbox_accessCode_name).clear()
        self.driver.find_element(By.XPATH, self.textbox_accessCode_name).send_keys(passcode)
        self.driver.find_element(By.XPATH, self.button_validateCode_name).click()

    def clickGetStartedButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.button_getStarted_name)))
        self.driver.find_element(By.XPATH, self.button_getStarted_name).click()

    def setAccountTextField(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.button_AccountSubmit_name)))
        self.driver.find_element(By.XPATH, self.textbox_FirstName_Class).send_keys(self.textbox_FirstName_Value)
        self.driver.find_element(By.XPATH, self.textbox_LastName_Class).send_keys(self.textbox_LastName_Value)
        self.driver.find_element(By.XPATH, self.textBox_DOB_Class).send_keys(self.textBox_DOB_Value)
        self.driver.find_element(By.XPATH, self.textBox_DOB_Class).send_keys(Keys.TAB)

        # ActionChains(self.driver.find_element(By.XPATH, self.textBox_DOB_Class).send_keys(Keys.TAB * 1))
        # self.ActionChains(self.driver.find_element(By.XPATH, self.textBox_DOB_Class)).send_keys(Keys.TAB)
        # ActionChains.perform()
        # self.driver.find_element(By.XPATH, self.textBox_DOB_Class).click()
        # time.sleep(1.0)

    def setAccountTextField1(self):
        self.driver.find_element(By.XPATH, self.textbox_SSN_Class).send_keys(self.textbox_SSN_Value)
        self.driver.find_element(By.XPATH, self.textbox_SSNRecheck_Class).send_keys(self.textbox_SSN_Value)
        self.driver.find_element(By.XPATH, self.textbox_zip_Class).send_keys(self.textbox_zip_Value)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.button_AccountSubmit_name).click()
