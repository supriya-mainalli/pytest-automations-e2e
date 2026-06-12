from playwright.sync_api import Page, expect


def test_login_orangehrm(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()

def test_placeholder(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # placeholder
    page.get_by_placeholder("Hide/Show Example").fill("supriya")
    # page.wait_for_timeout(3000)
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    page.locator("#show-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    page.locator("#name").fill('supriya')
    # alert popups
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    #iframe
    new_page = page.frame_locator("#courses-iframe")
    new_page.get_by_role("link", name="All Access Plan").click()
    text = new_page.get_by_role("heading", name="All Access").text_content()
    assert text=="All Access Subscription"
