import pytest
from pages.login_page import LoginPage


class TestLogin:

    def test_successful_login(self, page, base_url):
        login = LoginPage(page)
        login.navigate(base_url)
        login.login("standard_user", "secret_sauce")

        assert page.url.endswith("/inventory.html"), "Should redirect to inventory"

    def test_invalid_credentials(self, page, base_url):
        login = LoginPage(page)
        login.navigate(base_url)
        login.login("wrong_user", "wrong_pass")

        assert login.is_error_visible()
        assert "do not match" in login.get_error_message()

    def test_empty_username(self, page, base_url):
        login = LoginPage(page)
        login.navigate(base_url)
        login.login("", "secret_sauce")

        assert "Username is required" in login.get_error_message()

    def test_empty_password(self, page, base_url):
        login = LoginPage(page)
        login.navigate(base_url)
        login.login("standard_user", "")

        assert "Password is required" in login.get_error_message()

    def test_locked_out_user(self, page, base_url):
        login = LoginPage(page)
        login.navigate(base_url)
        login.login("locked_out_user", "secret_sauce")

        assert "locked out" in login.get_error_message().lower()
