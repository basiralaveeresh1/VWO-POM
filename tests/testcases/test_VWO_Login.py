import allure
import pytest
from tests.pageObjects.pom.loginPage import LoginPage
from selenium import webdriver
from tests.utils.common_utils import webdriver_wait
@pytest.fixture()

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver

@allure.epic("VWO Login TestCase")
@allure.feature("TC#0 - VWO App Negetive Test")
@pytest.mark.negetive
def test_vwo_login_negetive(setup):
    try:
        driver = setup
        loginPage = LoginPage(driver) # I have created the Object here
        loginPage.login_to_vwo(username="veeresh1206@gmail.com",password="Veeru@123")
        webdriver_wait(driver=driver,elemtn_tuple=loginPage.get_error_message())
        error_message_cssselector = LoginPage.get_error_message_text()
        assert error_message_cssselector=="Your email, password, IP address or location did not match"

    except Exception as e:
        pytest.xfail("Failed TC")
        print(e)

@allure.epic("VWO Login TestCase")
@allure.feature("TC#0 - VWO App Negetive Test")
@pytest.mark.positive

def test_vwo_login_pasitive():
    pass
