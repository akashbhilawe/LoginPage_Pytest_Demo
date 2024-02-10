import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjects.UserLogin import LoginClass
from utilities.Logger import LoggenClass
from utilities.readconfig import Readconfig


class Test_UserLogin:
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    log = LoggenClass.log_generator()

    @allure.feature('page_title')
    @allure.story('Verifying the page title')
    @allure.issue('ABC-123')
    @allure.link(' https://admin-demo.nopcommerce.com/', name='Orange HRM Website')
    @allure.title('NonCom - Test page_title')
    @allure.description('My test description')
    @allure.link('https://www.example.com')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_verify_url_001(self, setup):
        self.log.info("Test_case test_verify_url_001 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.log.info("Page Title is --> " + self.driver.title)
        # print(self.driver.title)
        if self.driver.title == "Your store. Login":
            self.log.info("Test_Case test_verify_url_001 is passed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_verify_url_001-Pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_pass.png")
            assert True
        else:
            self.log.info("Test_Case test_verify_url_001 is failed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_verify_url_001-Fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_fail.png")
            assert False
        self.log.info("Test_case test_verify_url_001 is Completed")

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_user_login_002(self, setup):
        self.log.info("Test_case test_user_login_002 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.log.info("Entering email - " + self.username)
        self.lp.Enter_Username(self.username)
        self.log.info("Entering Password - " + self.password)
        self.lp.Enter_Password(self.password)
        self.log.info("Click on login button")
        self.lp.Click_Login()
        if self.lp.Verify_Login_Status() == "Login Pass":
            self.log.info("Test_case test_user_login_002 is passed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_002-Pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_pass.png")
            self.log.info("Click on Logout button")
            self.lp.Click_Logout()
            assert True
        else:
            self.log.info("Test_case test_user_login_002 is Failed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_002-Fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_fail.png")
            assert False
        self.log.info("Test_case test_user_login_002 is Completed")


# pytest -v -n=2 -m sanity --alluredir="C:\WebTesting\LoginPage_Pytest\AllureReport" -p no:warnings