from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    employee_status = (By.CSS_SELECTOR, "#inlineRadio1")
    accepet_form = (By.XPATH, "//input[@type= 'submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getchekbox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getemployee_status(self):
        return self.driver.find_element(*HomePage.employee_status)

    def getaccept(self):
        return self.driver.find_element(*HomePage.accepet_form)

    def getalert(self):
        return self.driver.find_element(*HomePage.alert)

