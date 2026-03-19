import pytest
from pages.inventory_page import InventoryPage


class TestInventory:

    def test_six_products_displayed(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)

        assert inventory.is_loaded()
        assert inventory.get_item_count() == 6, "Should display 6 products"

    def test_add_item_to_cart(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_item_to_cart("sauce-labs-backpack")

        assert inventory.get_cart_count() == 1

    def test_add_multiple_items_to_cart(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        inventory.add_item_to_cart("sauce-labs-bike-light")

        assert inventory.get_cart_count() == 2

    def test_cart_navigation(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.go_to_cart()

        assert logged_in_page.url.endswith("/cart.html")
