from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver


    # cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
    card_title = (By.CSS_SELECTOR, ".card-title a")
    # self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    btn_primary = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    #self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
    btn_success = (By.CSS_SELECTOR, "button[class*='btn-success']")


    def getCardtitle(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)

    def getBtnPrimary(self):
        return self.driver.find_element(*CheckoutPage.btn_primary)

    def getBtnSuccess(self):
        self.driver.find_element(*CheckoutPage.btn_success).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage