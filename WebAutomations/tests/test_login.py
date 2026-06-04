import logging

import pytest
import allure
from WebAutomations.pages.login_page import LoginPage

@allure.feature("OrangeHRM Login Tests")
@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.testId001
    def test_success_login(self):
        """Test case for a valid login."""
        login = LoginPage(self.driver)
        with allure.step("Open login page"):
            login.login('Admin', 'admin123')