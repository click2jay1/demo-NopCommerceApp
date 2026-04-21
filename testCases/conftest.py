import pytest
import undetected_chromedriver as uc


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setupdriver(browser):
    if browser == 'chrome':
        options = uc.ChromeOptions()

        # Adding common arguments to help bypass detection
        options.add_argument("--disable-blink-features=AutomationControlled")

        # undetected-chromedriver handles 'excludeSwitches' and 'useAutomationExtension' automatically
        driver = uc.Chrome(options=options, version_main=145, use_subprocess=True)

    elif browser == 'firefox':
        # For Firefox, detection is harder to bypass; Chrome with UC is generally more successful
        from selenium import webdriver
        driver = webdriver.Firefox()
    else:
        from selenium import webdriver
        driver = webdriver.Ie()

    driver.maximize_window()
    yield driver  # ✅ IMPORTANT
    driver.quit()  # ✅ CLEANUP