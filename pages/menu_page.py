
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    live_classes = (By.XPATH, "//p[normalize-space()='LIVE Classes']")
    courses = (By.XPATH, "//p[normalize-space()='Courses']")
    practice = (By.XPATH, "//p[normalize-space()='Practice']")
    chat_widget = (By.ID, "zs_fl_chat")

    def is_live_classes_visible(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.live_classes)
        )
        return element.is_displayed()

    def is_courses_visible(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.courses)
        )
        return element.is_displayed()

    def is_practice_visible(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.practice)
        )
        return element.is_displayed()

    def is_chat_widget_visible(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.chat_widget)
        )
        return element.is_displayed()