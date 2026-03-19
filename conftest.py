import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.saucedemo.com"


@pytest.fixture
def logged_in_page(page, base_url):
    page.goto(base_url)
    page.fill("[data-test='username']", "standard_user")
    page.fill("[data-test='password']", "secret_sauce")
    page.click("[data-test='login-button']")
    page.wait_for_url("**/inventory.html")
    yield page
    page.context.clear_cookies()
