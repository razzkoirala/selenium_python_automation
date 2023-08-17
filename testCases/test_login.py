import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import Login



class Test_001_Login:
    baseURL = "https://hotfix.sandbox.my.site.com/onboarding/s/"
    username = "dev"
    passcode = "123123123"
    button_xpath = '//button[contains(@class, "slds-button slds-button_brand") and contains(text(), "Acknowledge")]'
    input_accesscode_name = '//input[contains(@class, "slds-input") and contains(@name,"accessCode")]'
    button_getStarted_name = '//button[contains(@class, "slds-button slds-button_brand") and contains(text(), "Get Started")]'

    ####
    # def test_homepageTitle(self, setup):
    #     self.driver= setup
    #     self.driver.get(self.baseURL)
    #     act_title = self.driver.title
    #    # self.driver.close()
    #     pageTitle1 = "TSP: Set up new login for My Account"
    #     if act_title == pageTitle1:
    #         self.driver.close()
    #         assert True
    #     else:
    #         assert False
    #         self.driver.close()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.button_xpath)))

        #self.driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        self.lp.clickAcknowledgementSelector()

        # Wait for Access Code Entry for 10 Sec and add code
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.input_accesscode_name)))
        self.lp.setpasscode(self.passcode)

        #wait to getStarted button fully load and click

        self.lp.clickGetStartedButton()
        self.lp.setAccountTextField()
        self.lp.setAccountTextField1()
