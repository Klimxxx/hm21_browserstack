import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_end():
    load_dotenv()


@pytest.fixture(scope='function')
def mobile_management(request):
    user_name = os.getenv('USER_NAME')
    access_key = os.getenv('ACCESS_KEY')

    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": user_name,
            "accessKey": access_key
        }
    })

    # browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    # либо этот сверху либо две строчки снизу вариант передачи драйвера
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options
    # селен верхние две строчки сам преобразуем в верхнюю одну

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()

@pytest.fixture(scope='function', autouse=True)
def setup_and_teardown_browser(request, mobile_management):

    yield
