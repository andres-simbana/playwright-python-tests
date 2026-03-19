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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")
        if page:
            import os
            os.makedirs("reports/screenshots", exist_ok=True)
            page.screenshot(path=f"reports/screenshots/{item.name}.png", full_page=True)
