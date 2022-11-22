from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver
    # self.driver.find_element(By.ID, "country").send_keys("Ind")
    submit = (By.ID, "country")
    # self.driver.find_element(By.LINK_TEXT, "India").click()
    country = (By.LINK_TEXT, "India")
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
    purchase = (By.XPATH, "//input[@value='Purchase']")
    # self.driver.find_element(By.CLASS_NAME, "alert-dismissible")
    alert = (By.CLASS_NAME, "alert-dismissible")

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getAlert(self):
        return self.driver.find_element(*ConfirmPage.alert)