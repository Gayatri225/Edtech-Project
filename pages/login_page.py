
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    email_input = (By.ID, "email")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-btn")

    error_message = (
        By.XPATH,
        "//*[contains(text(),'Invalid') or "
        "contains(text(),'invalid') or "
        "contains(text(),'incorrect') or "
        "contains(text(),'Incorrect') or "
        "contains(text(),'wrong') or "
        "contains(text(),'Wrong')]"
    )

    profile_menu = (
        By.XPATH,
        "//img[@alt='Profile']/ancestor::div[contains(@class,'account-box-toggler')]"
    )

    sign_out_option = (
        By.XPATH,
        "//p[normalize-space()='Sign Out']"
    )

    def enter_email(self, email):
        field = self.wait.until(
            EC.visibility_of_element_located(self.email_input)
        )
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_error_message_displayed(self):
        try:
            error = self.wait.until(
                EC.visibility_of_element_located(self.error_message)
            )
            return error.is_displayed()

        except TimeoutException:
            return False

    def click_profile_menu(self):
        profile = self.wait.until(
            EC.element_to_be_clickable(self.profile_menu)
        )
        profile.click()

    def click_sign_out(self):
        sign_out = self.wait.until(
            EC.element_to_be_clickable(self.sign_out_option)
        )
        sign_out.click()

    def get_current_url(self):
        return self.driver.current_url