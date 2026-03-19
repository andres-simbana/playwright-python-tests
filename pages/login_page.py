from playwright.sync_api import Page, Locator


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input: Locator = page.locator("[data-test='username']")
        self.password_input: Locator = page.locator("[data-test='password']")
        self.login_button: Locator = page.locator("[data-test='login-button']")
        self.error_message: Locator = page.locator("[data-test='error']")

    def navigate(self, base_url: str):
        self.page.goto(base_url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_message.text_content()

    def is_error_visible(self) -> bool:
        return self.error_message.is_visible()
