import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHome(BaseClass):

    def test_form_submission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homepage.getname().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["email"])
        homepage.getpassword().send_keys(12345)
        homepage.getchekbox().click()
        # Static Dropdown
        self.SelectOptionByText(homepage.getgender(), getData["gender"])
        homepage.getemployee_status().click()
        homepage.getaccept().click()
        message = homepage.getalert().text
        assert ("Success" in message)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("Testcase1"))
    def getData(self, request):
        return request.param
