import time

import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from utilities.businessFlows import CustomerFlows
from pageObjects.addNewCustomerPOM import AddNewCustomerPOM
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestData.create_email_password import Emailpasswordcreator

class TestCase_004_AddNewCustomer:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    generated_email = ""

    @pytest.fixture(autouse=True)
    def set_logger(self, request):
        test_name = request.node.name
        self.logger = LogGeneration.loggen(test_name)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_004_add_new_customer(self, setupdriver):
        self.driver = setupdriver
        login = CustomerFlows(self.driver,self.base_url, self.username, self.password)
        self.logger.info("*** Login Starts ***")
        login.login()
        self.logger.info("*** Login Ends ***")

        wait = WebDriverWait(self.driver, 30)
        ac = AddNewCustomerPOM(self.driver)
        ac.new_customers_form()
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Customers']"))
        )
        self.logger.info("*** Click on Add Button ***")
        ac.click_addNew_btn()
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='AdminComment']"))
        )

        # Get an username and password
        nc = Emailpasswordcreator(8)
        email = nc.create_email()
        password = nc.create_password()

        # Now enter the customer details
        self.logger.info("*** Entering the customer details ***")
        ac.enter_email(email)
        time.sleep(2)
        ac.enter_password(password)
        time.sleep(2)
        ac.enter_firstName("Sarah")
        ac.enter_lastName("Oscar")
        ac.set_gender_female()
        ac.enter_companyName("Sarah Corp")
        ac.set_customerRoles("Administrators")
        ac.set_customerRoles("Registered")
        ac.managerOfVendor("Not a vendor")
        ac.set_changePassword()
        ac.set_admComments("I am a new User")
        ac.click_save()
        time.sleep(5)
        print("\nEmail is: ", email)
        found, name = login.only_search_customer_by_email(email)
        assert found, "❌ Customer not found"
        self.logger.info("*** Customer 'Sarah Oscar' is added Successfully ***")
        print(f"\n✔️ Customer 'Sarah Oscar' is added Successfully !!")
        self.driver.quit()


