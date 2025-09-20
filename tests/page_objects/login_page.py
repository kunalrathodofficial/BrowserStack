from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds timeout
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-btn")

        self.apple_filter_button = (By.XPATH, "//*[@id='__next']/div/div/main/div[1]/div[1]/label/span")
        self.product_count = (By.XPATH, "//*[@class='products-found']/span")

    def enter_username(self, username):
        elem = self.wait.until(EC.element_to_be_clickable(self.username_input))
        elem.click()
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.wait.until(EC.element_to_be_clickable(self.password_input))
        elem.click()
        elem.send_keys(password)

    def click_login(self):
        elem = self.wait.until(EC.element_to_be_clickable(self.login_button))
        elem.click()

    def appleCLick(self):
        elem = self.wait.until(EC.element_to_be_clickable(self.apple_filter_button))
        elem.click()

    @property
    def productCount(self):
        elem = self.wait.until(EC.element_to_be_clickable(self.product_count))
        text = elem.text
        print(text)
        return text
