import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:

    def test_cart_is_empty_on_fresh_login(self, logged_in_page):
        logged_in_page.goto("https://www.saucedemo.com/cart.html")
        cart = CartPage(logged_in_page)

        assert cart.get_item_count() == 0

    def test_added_item_appears_in_cart(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        assert cart.get_item_count() == 1
        assert "Sauce Labs Backpack" in cart.get_item_names()

    def test_remove_item_from_cart(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        cart.remove_item(index=0)

        assert cart.get_item_count() == 0

    def test_proceed_to_checkout(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        cart.proceed_to_checkout()

        assert "checkout-step-one" in logged_in_page.url
