
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators
    login_button = (By.ID, "login-btn")

    signup_button = (
        By.XPATH,
        "//button[normalize-space()='Sign up']"
    )

    # Methods for Test Case 1
    def get_current_url(self):
        return self.driver.current_url

    # Methods for Test Case 2
    def get_page_title(self):
        return self.driver.title

    # Methods for Test Case 3
    def is_login_button_visible(self):
        login = self.wait.until(
            EC.visibility_of_element_located(self.login_button)
        )
        return login.is_displayed()

    def is_login_button_clickable(self):
        login = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )
        return login.is_enabled()

    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    # Methods for Test Case 4
    def is_signup_button_visible(self):
        signup = self.wait.until(
            EC.visibility_of_element_located(self.signup_button)
        )
        return signup.is_displayed()

    def is_signup_button_clickable(self):
        signup = self.wait.until(
            EC.element_to_be_clickable(self.signup_button)
        )
        return signup.is_enabled()

    def click_signup_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.signup_button)
        ).click()

    def get_signup_url(self):
        return self.driver.current_url
        