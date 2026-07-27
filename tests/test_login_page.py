
import os
from dotenv import load_dotenv

from pages.home_page import HomePage
from pages.login_page import LoginPage


load_dotenv()


class TestLoginPage:

    # Test Case 6
    def test_valid_login(self, driver):

        email = os.getenv("GUVI_EMAIL")
        password = os.getenv("GUVI_PASSWORD")

        assert email is not None, "GUVI_EMAIL is missing from .env"
        assert password is not None, "GUVI_PASSWORD is missing from .env"

        home = HomePage(driver)
        home.click_login_button()

        home.wait.until(
            lambda browser: "sign-in" in browser.current_url.lower()
        )

        login_page = LoginPage(driver)
        login_page.login(email, password)

        login_page.wait.until(
            lambda browser: "sign-in" not in browser.current_url.lower()
        )

        assert "sign-in" not in driver.current_url.lower()

    # Test Case 7
    def test_invalid_login(self, driver):

        home = HomePage(driver)
        home.click_login_button()

        home.wait.until(
            lambda browser: "sign-in" in browser.current_url.lower()
        )

        login_page = LoginPage(driver)

        login_page.login(
            "invaliduser12345@gmail.com",
            "WrongPassword123"
        )

        assert "sign-in" in driver.current_url.lower()
        assert login_page.is_error_message_displayed()

    # Test Case 10
    def test_logout(self, driver):

        email = os.getenv("GUVI_EMAIL")
        password = os.getenv("GUVI_PASSWORD")

        assert email is not None, "GUVI_EMAIL is missing from .env"
        assert password is not None, "GUVI_PASSWORD is missing from .env"

        home = HomePage(driver)
        home.click_login_button()

        home.wait.until(
            lambda browser: "sign-in" in browser.current_url.lower()
        )

        login_page = LoginPage(driver)
        login_page.login(email, password)

        login_page.wait.until(
            lambda browser: "sign-in" not in browser.current_url.lower()
        )

        login_page.click_profile_menu()
        login_page.click_sign_out()

        login_page.wait.until(
            lambda browser:
            "sign-in" in browser.current_url.lower()
            or browser.current_url.lower() in [
                "https://www.guvi.in/",
                "https://www.guvi.in"
            ]
        )

        current_url = driver.current_url.lower()

        assert (
            "sign-in" in current_url
            or current_url == "https://www.guvi.in/"
            or current_url == "https://www.guvi.in"
        )