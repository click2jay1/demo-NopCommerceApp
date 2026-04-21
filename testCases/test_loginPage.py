import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration

class Test_001_Login:
    base_url = ReadConfig.getApplicationURL() #Reading URL from readProperties file
    username = ReadConfig.getUsername()  # Reading username from readProperties file
    password = ReadConfig.getPassword()  # Reading password from readProperties file

    @pytest.fixture(autouse=True)
    def setup_logger(self, request):
        test_name = request.node.name
        self.logger = LogGeneration.loggen(test_name)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Test001_HomePageTitle(self, setupdriver):
        self.logger.info("************** Test_001_Login ***************")
        expected_title = "nopCommerce demo store. Login"
        self.driver = setupdriver
        try:
            self.driver.delete_all_cookies()
            self.driver.get(self.base_url)
            WebDriverWait(self.driver,30).until(
                EC.title_contains("nopCommerce")
            )
            actual_title = self.driver.title
            self.logger.info("************* Verifying Home page Title ***************")
            assert actual_title == expected_title, "Title Not matched"
            self.logger.info("************* Home page Title Verified ***************")
        finally:
            self.driver.quit()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Test001_login(self, setupdriver):
        self.driver = setupdriver
        wait = WebDriverWait(self.driver, 10)
        self.logger.info("************* Verifying Login Test ***************")
        try:
            self.driver.delete_all_cookies()
            self.driver.get(self.base_url)
            self.lp = LoginPage(self.driver)
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.login_button()
            assert wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "content-header"))
            ).is_displayed(), "Login Failed"
            self.driver.save_screenshot(".\\ScreenShots\\" + "screenshot.png")


        except TimeoutException as e:
            self.logger.error("************** Login Test Failed ****************")
            print(f"ERROR: Timeout Happened - {str(e)}")
            raise

        except ValueError as ve:
            print(f"ERROR: Value Error occurred - {str(ve)}")
            self.logger.error("************* Login Test Failed ***************")
            raise
        finally:
            self.driver.quit()
            self.logger.info("************** Login Test Completed ****************")
