import time
import pytest
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from utilities import xlUtilities

class Test_002_Login:
    base_url = ReadConfig.getApplicationURL() #Reading URL from readProperties file
    path = ".//TestData/loginData.xlsx"

    @pytest.fixture(autouse=True)
    def setup_logger(self, request):
        test_name = request.node.name
        self.logger = LogGeneration.loggen(test_name)


    @pytest.mark.regression
    def test_Test002_login(self, setupdriver):
        self.driver = setupdriver
        wait = WebDriverWait(self.driver, 50)
        self.logger.info("*************** Test_002_DDT_Login *******************")
        self.rows = xlUtilities.getRowCount(self.path, "Sheet1")
        print(f"\nNumber of rows: {self.rows}")
        status_list = []
        expected_title = "Dashboard / nopCommerce administration"

        for r in range(2,self.rows+1):
            print(f"\nvalue of 'r': {r}")
            self.username = xlUtilities.readData(self.path, 'Sheet1', r, 1)
            print(f"Username: {self.username}")
            self.password = xlUtilities.readData(self.path, 'Sheet1', r, 2)
            print(f"Password: {self.password}")
            self.exp = xlUtilities.readData(self.path, 'Sheet1', r, 3)
            print(f"Expected result: {self.exp}")

            self.driver.delete_all_cookies()
            self.driver.get(self.base_url)
            self.logger.info(f"*** Number {r - 1} entry starts ****")
            wait.until(EC.presence_of_element_located((By.ID, "Email")))
            self.logger.info(f"*** Number {r - 1} entry ends ****")
            self.logger.info(f"*** Number {r - 1} Login check starts ****")

            try:
                self.lp = LoginPage(self.driver)
                time.sleep(3)
                self.lp.set_username(self.username)
                time.sleep(2)
                self.lp.set_password(self.password)
                time.sleep(2)
                self.lp.login_button()

                wait.until(EC.title_contains("nopCommerce"))
                actual_title = self.driver.title
                print(f"Expected Title: {expected_title}")
                print(f"Actual Title: {actual_title}")


                if actual_title == expected_title:
                    result = "pass"
                    if result == self.exp.lower():
                        status_list.append("Pass")
                        self.logger.info(f"*** Combination number {r-1} is Passed ***")
                    else:
                        status_list.append("Fail")
                        self.logger.info(f"*** Combination number {r-1} is failed ***")


                else:
                    result = "fail"
                    if result == self.exp.lower():
                        status_list.append("Pass")
                        self.logger.info(f"*** Combination number {r-1} is Passed ***")
                    else:
                        status_list.append("Fail")
                        self.logger.info(f"*** Combination number {r-1} is Failed ***")

                print(f"Status List: {status_list}")
                print(f"Result Value: {result}")

            except TimeoutException as e:
                self.logger.error("************** Login Test Failed ****************")
                print(f"ERROR: Timeout Happened - {str(e)}")
                raise

            except ValueError as ve:
                print(f"ERROR: Value Error occurred - {str(ve)}")
                self.logger.error("************* Login Test Failed ***************")
                raise

            finally:
                print(f"*** Number {r-1} Login check is done ****")
                self.logger.info(f"*** Number {r-1} Login check is done ****")
                try:
                    logout_buttons = self.driver.find_elements(By.LINK_TEXT, "Logout")

                    if len(logout_buttons) > 0:
                        self.lp.logout()
                        wait.until(EC.presence_of_element_located((By.ID, "Email")))
                    else:
                        self.logger.info("Logout button not found - moving to next iteration")

                except Exception as e:
                    self.logger.warning(f"Skipping logout due to error: {str(e)}")

        self.driver.quit()

        print(f"Final Status list: {status_list}")
        if "Fail" not in status_list:
            self.logger.info("******* DDT Login Test Pass ********")
            assert True
        else:
            self.logger.info("****** DDT Login Test Fail *******")
            assert False

        self.logger.info("************** Login Test Completed ****************")



