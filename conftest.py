import pytest
import os

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.saucedemo.com"


@pytest.fixture
def logged_in_page(page, base_url):
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.navigate(base_url)
    login.login(VALID_USERNAME, VALID_PASSWORD)
    page.wait_for_url("**/inventory.html")
    yield page
    page.context.clear_cookies()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when in ("call", "setup") and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            page.screenshot(path=f"reports/screenshots/{item.name}.png", full_page=True)
