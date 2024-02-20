from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text, driver):
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=f"new UiScrollable(new UiSelector().scrollable("
                                                                   f"true).instance(0)).scrollIntoView(new "
                                                                   f"UiSelector().textContains({text}).instance("
                                                                   f"0))").click()

    @staticmethod
    def swipeUp(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipeDown(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipeLeft(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipeRight(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)
