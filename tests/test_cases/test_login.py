import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from tests.page_objects.login_page import LoginPage
from tests.utils import config

@pytest.fixture
def driver():
    chrome_options = Options()
    # Use webdriver-manager to install and manage the correct version
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_login(driver):
    driver.get(config.BASE_URL)

    login = LoginPage(driver)
    login.appleCLick()
    time.sleep(7)
    count = login.product_count()
    print(count)


    #
    # time.sleep(7)
    # login.enter_username(config.USERNAME)
    # time.sleep(2)
    # login.enter_password(config.PASSWORD)
    # time.sleep(2)
    # driver.execute_script("window.scrollBy(0, -200);")
    # login.click_login()
    # time.sleep(10)
    # assert "health-check/network" in driver.current_url
