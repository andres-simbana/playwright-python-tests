from playwright.sync_api import Page, Locator


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items: Locator = page.locator(".cart_item")
        self.checkout_button: Locator = page.locator("[data-test='checkout']")
        self.continue_shopping: Locator = page.locator("[data-test='continue-shopping']")
        self.remove_buttons: Locator = page.locator("[data-test^='remove']")
        self.item_names: Locator = page.locator(".inventory_item_name")

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def get_item_names(self) -> list[str]:
        return self.item_names.all_text_contents()

    def remove_item(self, index: int = 0):
        self.remove_buttons.nth(index).click()

    def proceed_to_checkout(self):
        self.checkout_button.click()
        self.page.wait_for_url("**/checkout-step-one.html")

    def go_back_to_shopping(self):
        self.continue_shopping.click()
        self.page.wait_for_url("**/inventory.html")
