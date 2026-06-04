from selenium.webdriver.common.by import By


class LoginLocators:
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")

    
