import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #Locators:
    textbox_username_id = "//input[@id='Email']"
    textbox_password_id = "//input[@id='Password']"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_linkText = "Logout"


    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_username_id))
        )
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)

    def set_password(self, password):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_password_id))
        )
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def login_button(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
        )
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logout(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_logout_linkText))
        )
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linkText).click()

