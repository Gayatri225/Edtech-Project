
from pages.menu_page import MenuPage


class TestMenuPage:

    # Test Case 8
    def test_verify_menu_items(self, driver):

        menu_page = MenuPage(driver)

        assert menu_page.is_live_classes_visible()
        assert menu_page.is_courses_visible()
        assert menu_page.is_practice_visible()

    # Test Case 9
    def test_verify_chat_widget(self, driver):

        menu_page = MenuPage(driver)

        assert menu_page.is_chat_widget_visible()