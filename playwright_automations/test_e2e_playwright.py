from playwright.sync_api import Playwright, expect
from playwright_automations.api_base import APIUtils

def test_e2e(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("supriyam@yopmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.locator("#login").click()

    api_utils = APIUtils()
    response = api_utils.add_to_cart(playwright)
    print(response['message'])
    assert str(response['message']) == "Product Added To Cart"

