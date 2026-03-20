from playwright.sync_api import Page, Locator


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_list: Locator = page.locator(".inventory_list")
        self.inventory_items: Locator = page.locator(".inventory_item")
        self.cart_badge: Locator = page.locator(".shopping_cart_badge")
        self.cart_link: Locator = page.locator(".shopping_cart_link")

    def is_loaded(self) -> bool:
        return self.inventory_list.is_visible()

    def get_item_count(self) -> int:
        return self.inventory_items.count()

    def add_item_to_cart(self, item_id: str):
        self.page.locator(f"[data-test='add-to-cart-{item_id}']").click()

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            count_text = self.cart_badge.inner_text()
            return int(count_text) if count_text else 0
        return 0

    def go_to_cart(self):
        self.cart_link.click()
        self.page.wait_for_url("**/cart.html")
