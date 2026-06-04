import time
import allure
import pytest
from selenium import webdriver

from config import read_configurations


@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    url = read_configurations('basic info', 'endpoint')
    driver.get(url)
    time.sleep(5)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.cls.driver

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
