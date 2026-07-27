
from pages.home_page import HomePage


class TestHomePage:

    # Test Case 1
    def test_verify_url(self, driver):

        home = HomePage(driver)

        expected_url = "https://www.guvi.in/"
        actual_url = home.get_current_url()

        assert actual_url == expected_url

    # Test Case 2
    def test_verify_title(self, driver):

        home = HomePage(driver)

        expected_title = "HCL GUVI | Learn to code in your native language"
        actual_title = home.get_page_title()

        assert actual_title == expected_title

    # Test Case 3
    def test_verify_login_button(self, driver):

        home = HomePage(driver)

        assert home.is_login_button_visible()
        assert home.is_login_button_clickable()

        home.click_login_button()

        home.wait.until(
            lambda browser: "sign-in" in browser.current_url.lower()
        )

        assert "sign-in" in driver.current_url.lower()

    # Test Case 4
    def test_verify_signup_button(self, driver):

        home = HomePage(driver)

        assert home.is_signup_button_visible()
        assert home.is_signup_button_clickable()

        home.click_signup_button()

        home.wait.until(
            lambda browser: "register" in browser.current_url.lower()
        )

        assert "register" in driver.current_url.lower()

    # Test Case 5
    def test_verify_signup_page_url(self, driver):

        home = HomePage(driver)

        home.click_signup_button()

        home.wait.until(
            lambda browser: "register" in browser.current_url.lower()
        )

        actual_url = home.get_signup_url()

        assert "https://www.guvi.in/register/" in actual_url