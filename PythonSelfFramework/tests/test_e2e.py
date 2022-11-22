from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopitems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardtitle()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.getBtnPrimary().click()
        confirmpage = checkoutpage.getBtnSuccess()
        log.info("Entering country name as ind")
        confirmpage.getSubmit().send_keys("Ind")
        self.verify_link_presence("India")
        confirmpage.getCountry().click()
        confirmpage.checkBox().click()
        confirmpage.getPurchase().click()
        success_text = confirmpage.getAlert().text
        log.info("Text received from application is " + success_text)
        assert "Success! Thank you!" in success_text



