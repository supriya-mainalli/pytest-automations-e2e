from WebAutomations.locators.login_page import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*LoginLocators.username).send_keys(username)
        self.driver.find_element(*LoginLocators.password).send_keys(password)
        self.driver.find_element(*LoginLocators.login_button).click()