from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


# Using app: https://play.google.com/store/apps/details?id=com.ambertech.amber
# Start server command:
# appium server -p 9000 -a 127.0.0.1 -pa /wd/hub


class TestLoginRegisterForm:
    session = 'http://127.0.0.1:9000/wd/hub'
    capabilities = {"platformName": "android", "appium:automationName": "uiautomator2", "appium:deviceName": "4a97c487",
                    } # 'unicodeKeyboard': 'true', 'resetKeyboard': 'true'

    def setup(self) -> None:
        self.driver = webdriver.Remote(self.session, self.capabilities)

    def teardown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_get_started(self) -> None:
        """
        Testing full circle of Get Started process at first running app.
        Result: the phone registration window. There is choosing in window: enter phone or sign up with Apple / Google.
        """
        def click_continue_button():
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='continue').click()

        # Press "get started" button
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="get started"]').click()
        # Get the countries list
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="+93"]').click()
        self.driver.implicitly_wait(10)
        # Search current country
        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').click()
        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').send_keys('Georgia')
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="Georgia"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="continue"]').click()
        self.driver.implicitly_wait(10)
        # Choose the language (don't change the locator string!)
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="""🇺🇸
english""").click()
        click_continue_button()
        # Choose age
        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').click()
        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').send_keys('28')
        click_continue_button()


