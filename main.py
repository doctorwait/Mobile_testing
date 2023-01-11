from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Start server command:
# appium server -p 9000 -a 127.0.0.1 -pa /wd/hub


class TestLoginRegisterForm:
    session = 'http://127.0.0.1:9000/wd/hub'
    capabilities = {"platformName": "android", "appium:automationName": "uiautomator2", "appium:deviceName": "4a97c487"}

    def setup(self) -> None:
        self.driver = webdriver.Remote(self.session, self.capabilities)

    def teardown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_get_started(self) -> None:
        # Press "get started" button
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="get started"]').click()
        # Get the countries list
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="+93"]').click()
        self.driver.implicitly_wait(10)
        # Search current country
        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').click()
        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').send_keys('Georgia')
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Georgia').click()
        # Press 'continue" button
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="continue"]').click()


