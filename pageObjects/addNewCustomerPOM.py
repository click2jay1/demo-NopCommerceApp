import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class AddNewCustomerPOM:
    #Locators
    lnk_customers_menu_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    lnk_customers_menuItem_xpath = "(//p[contains(text(),'Customers')])[2]"
    button_add_new_xpath = "//a[normalize-space()='Add new']"
    txtBox_email_xpath = "//input[@id='Email']"
    txtBox_password_xpath = "//input[@id='Password']"
    txtBox_firstName_xpath = "//input[@id='FirstName']"
    txtBox_lastName_xpath = "//input[@id='LastName']"
    radioBtn_male_xpath = "//input[@id='Gender_Male']"
    radioBtn_female_xpath = "//input[@id='Gender_Female']"
    txtBox_CompanyName_xpath = "//input[@id='Company']"
    checkBox_IsTax_xpath = "//input[@id='Company']"
    txtBox_customerRole_xpath = "//input[@role='searchbox']"
    listItem_Admnstr_custRole_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-avap-1']"
    listItem_Modrtr_custRole_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-wf0h-2']"
    listItem_Registrd_custRole_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-esnp-3']"
    listItem_Guest_custRole_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-kp96-4']"
    listItem_Vendr_custRole_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-8vkd-5']"
    drpdwn_Mangr_vendr_xpath = "//span[@id='select2-VendorId-container']"
    drpdwn_notVendr_xpath = "//li[@id='select2-VendorId-result-5g09-0']"
    drpdwn_vendr1_xpath = "//li[@id='select2-VendorId-result-b05k-1']"
    drpdwn_vendr2_xpath = "//li[@id='select2-VendorId-result-vmha-2']"
    checkBox_active_xpath = "//input[@id='Active']"
    checkBox_MustChangePassword_xpath = "//input[@id='MustChangePassword']"
    txtBox_adminComment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def new_customers_form(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.lnk_customers_menu_xpath))
        )
        self.driver.find_element(By.XPATH, self.lnk_customers_menu_xpath).click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.lnk_customers_menuItem_xpath))
        )
        self.driver.find_element(By.XPATH, self.lnk_customers_menuItem_xpath).click()

    def click_addNew_btn(self):
        self.driver.find_element(By.XPATH, self.button_add_new_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.txtBox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBox_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.txtBox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBox_password_xpath).send_keys(password)

    def enter_firstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txtBox_firstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBox_firstName_xpath).send_keys(firstname)

    def enter_lastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtBox_lastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBox_lastName_xpath).send_keys(lastname)

    def set_gender_male(self):
        self.driver.find_element(By.XPATH, self.radioBtn_male_xpath).click()

    def set_gender_female(self):
        self.driver.find_element(By.XPATH, self.radioBtn_female_xpath).click()

    def enter_companyName(self, companyName):
        self.driver.find_element(By.XPATH, self.txtBox_CompanyName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtBox_CompanyName_xpath).send_keys(companyName)

    def set_isTax_exempt(self):
        self.driver.find_element(By.XPATH, self.checkBox_IsTax_xpath).click()

    def set_customerRoles(self, role):

        try:
            delete_buttons = self.driver.find_elements(By.XPATH, "//span[@title='delete']")
            for btn in delete_buttons:
                btn.click()
        except:
            pass
        self.driver.find_element(By.XPATH, "//input[@role='searchbox']").click()
        time.sleep(3)

        role_xpath = f"//li[contains(text(),'{role}')]"
        wait = WebDriverWait(self.driver, 10)
        self.listItem = wait.until(EC.element_to_be_clickable((By.XPATH, role_xpath)))
        self.driver.execute_script("arguments[0].click();", self.listItem)

        # self.driver.find_element(By.XPATH, "//span[@role='presentation'][normalize-space()='×']").click()
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, self.txtBox_customerRole_xpath).click()
        # time.sleep(3)
        #
        # if role == "Registered":
        #     self.listItem = self.driver.find_element(By.LINK_TEXT, "Registered")
        #
        # elif role == "Administrators":
        #     self.listItem = self.driver.find_element(By.LINK_TEXT, "Administrators")
        #
        # elif role == "Guest":
        #     #Here user can be either Registered or Guest, so first remove Registered as this is default value
        #     time.sleep(3)
        #     self.driver.find_element(By.XPATH, "//span[@role='presentation'][normalize-space()='×']").click()
        #     self.listItem = self.driver.find_element(By.XPATH, self.listItem_Guest_custRole_xpath)
        #
        # elif role == "Forum Moderators":
        #     self.listItem = self.driver.find_element(By.XPATH, self.listItem_Modrtr_custRole_xpath)
        #
        # elif role == "Vendor":
        #     self.listItem = self.driver.find_element(By.XPATH, self.listItem_Vendr_custRole_xpath)
        #
        # else :
        #     self.listItem = self.driver.find_element(By.XPATH, self.listItem_Guest_custRole_xpath)
        #
        # self.driver.execute_script("arguments[0].click();", self.listItem)


    def managerOfVendor(self, value):
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//b[@role='presentation']"))
        )
        dropdown.click()
        option_xpath = f"//li[contains(text(),'{value}')]"
        option = wait.until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        self.driver.execute_script("arguments[0].click();", option)

    def set_active(self):
        self.driver.find_element(By.XPATH, self.checkBox_active_xpath).click()

    def set_changePassword(self):
        self.driver.find_element(By.XPATH, self.checkBox_MustChangePassword_xpath).click()

    def set_admComments(self, comment):
        self.driver.find_element(By.XPATH, self.txtBox_adminComment_xpath).send_keys(comment)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()





















