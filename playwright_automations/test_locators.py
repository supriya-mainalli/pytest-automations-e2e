from playwright.sync_api import Page, expect


def test_login_orangehrm(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()
