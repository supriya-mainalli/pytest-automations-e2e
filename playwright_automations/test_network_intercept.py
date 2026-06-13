from playwright.sync_api import Playwright, expect
import time


# intercept response -> fulfill
data = {"data":[],"message":"No Orders"}
def network_intercept_response(route):
    route.fulfill(
        json = data
    )

def test_network_response_mock(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")

    # Intercept the network and mock the response
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", network_intercept_response)
    page.get_by_placeholder("email@example.com").fill("supriyam@yopmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(2)
    text = page.locator(".mt-4").text_content().strip()
    print(text)
    assert text == "You have No Orders to show at this time. Please Visit Back Us"


# intercept request
def network_intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a2d70c417ee3e78bada0ce2")

def test_network_request_mock(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")
    # Intercept the network and mock the response
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", network_intercept_request)
    page.get_by_placeholder("email@example.com").fill("supriyam@yopmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(2)
    page.get_by_role("button", name="View").first.click()
    text = page.locator(".blink_me").text_content().strip()
    assert text == "You are not authorize to view this order"
