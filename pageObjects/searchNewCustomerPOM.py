import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class SearchCustomers:
    #lnk_customers_menu_xpath = "(//a[@class='nav-link active'])[1]"
    lnk_customers_menu_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    lnk_customers_menuItem_xpath = "(//p[contains(text(),'Customers')])[2]"
    txtBox_email_xpath = "//input[@id='SearchEmail']"
    txt_FirstName_xpath = "//input[@id='SearchFirstName']"
    txt_LastName_xpath = "//input[@id='SearchLastName']"
    list_custRole_xpath = "(//li[@title='Registered'])[1]//span[@class='select2-selection__choice__remove']"
    btn_search_xpath = "//button[@id='search-customers']"


    def __init__(self, driver):
        self.driver = driver

    def new_customers_form(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menu_xpath).click()
        self.driver.find_element(By.XPATH, self.lnk_customers_menuItem_xpath).click()

    def remove_defaultRole(self):
        self.driver.find_element(By.XPATH, self.list_custRole_xpath).click()

    def searchByEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtBox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBox_email_xpath).send_keys(email)

    def searchByFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).send_keys(firstname)

    def searchByLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_LastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_LastName_xpath).send_keys(lastname)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()



