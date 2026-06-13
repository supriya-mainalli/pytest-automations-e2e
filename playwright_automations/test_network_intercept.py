from playwright.sync_api import Playwright, expect
import time

data = {"data":[],"message":"No Orders"}
def network_intercept(route):
    route.fulfill(
        json = data
    )

def test_network1(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")

    # Intercept the network and mock the response
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", network_intercept)
    page.get_by_placeholder("email@example.com").fill("supriyam@yopmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(2)
    text = page.locator(".mt-4").text_content().strip()
    print(text)
    assert text == "You have No Orders to show at this time. Please Visit Back Us"