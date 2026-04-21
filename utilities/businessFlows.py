import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.loginPage import LoginPage
from pageObjects.searchNewCustomerPOM import SearchCustomers

class CustomerFlows:

    def __init__(self, driver, base_url, username, password):
        self.driver = driver
        self.base_url = base_url
        self.username = username
        self.password = password


    def login(self):
        wait = WebDriverWait(self.driver, 60)
        self.driver.delete_all_cookies()
        self.driver.get(self.base_url)
        wait.until(EC.title_is("nopCommerce demo store. Login"))
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.login_button()

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='content-header']"))
        )


    def search_customer_by_email(self, email):
        wait = WebDriverWait(self.driver, 60)

        sc = SearchCustomers(self.driver)
        sc.new_customers_form()

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Customers']"))
        )
        # Now Removing the existing selection
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='Customer roles']"))
        )
        time.sleep(2)
        sc.remove_defaultRole()

        sc.searchByEmail(email) # Providing the email to search
        time.sleep(3)
        sc.clickOnSearch() # Clicking on the Search button
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//table"))
        )

        rows = self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr")

        for i in range(len(rows)):
            # Re-fetch
            rows = self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr")
            row = rows[i]
            email_val = row.find_element(By.XPATH, "./td[2]").text
            name_val = row.find_element(By.XPATH, "./td[3]").text

            if email_val == email:
                return True, name_val

        return False, None



    def search_customer_by_name(self, firstname, lastname):
        wait = WebDriverWait(self.driver, 60)
        name = firstname + " " + lastname
        print("***********")
        print(f"\nName is: {name}")
        print("***********")

        sc = SearchCustomers(self.driver)
        sc.new_customers_form()

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Customers']"))
        )
        # Now Removing the existing selection
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='Customer roles']"))
        )
        time.sleep(2)
        sc.remove_defaultRole()

        sc.searchByFirstName(firstname)  # Providing the FirstName to search
        time.sleep(3)
        sc.searchByLastName(lastname) # Providing the lastName to search
        time.sleep(3)
        sc.clickOnSearch()  # Clicking on the Search button
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//table"))
        )

        rows = self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr")

        for i in range(len(rows)):
            # Re-fetch
            rows = self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr")
            row = rows[i]
            #email_val = row.find_element(By.XPATH, "./td[2]").text
            name_val = row.find_element(By.XPATH, "./td[3]").text

            if name_val == name:
                return True, name_val

        return False, None


    def only_search_customer_by_email(self, email):
        wait = WebDriverWait(self.driver, 60)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='SearchEmail']"))
        )
        sc = SearchCustomers(self.driver)
        sc.searchByEmail(email) # Providing the email to search
        time.sleep(3)
        sc.clickOnSearch() # Clicking on the Search button
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//table"))
        )

        option_xpath = f"//table[@id='customers-grid']//td[normalize-space()='{email}']"
        email_val = wait.until(
            EC.presence_of_element_located((By.XPATH, option_xpath))
        )

        print("\nEmail is: ", email_val.text)

        if email_val.text == email:
            return True, email_val.text

        return False, None

