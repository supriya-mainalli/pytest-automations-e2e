from playwright.sync_api import Page, expect
import time


def test_chrome_launch01(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def test_firefox_launch02(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def test_login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("checkbox", name="I Agree to the terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    iphone_phone = page.locator("app-card").filter(has_text="iphone X")
    iphone_phone.get_by_role("button", name="Add").click()
    nokia_phone = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_phone.get_by_role("button", name="Add").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)



def test_invalid_login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("testjdhgs@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    time.sleep(5)
    page.get_by_role("checkbox", name="I Agree to the terms and conditions")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible


def test_child_window(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as child_window:
        page.locator(".blinkingText").filter(has_text="Free Access to").click()
        child_window_instance = child_window.value
        text = child_window_instance.get_by_role("heading", name="Documents request").text_content()
        assert text == "Documents request"
