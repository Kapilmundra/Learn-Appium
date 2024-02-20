import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.options.android import UiAutomator2Options

desired_caps = {'platformName': 'Android', 'deviceName': 'Android', 'appPackage': 'com.mobeta.android.demodslv',
                'appActivity': '.Launcher'}
capability_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://localhost:4723', options=capability_options)
driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.ID, value='com.mobeta.android.demodslv:id/activity_title')[0].click()

elements = driver.find_elements(by=AppiumBy.ID, value='com.mobeta.android.demodslv:id/drag_handle')

actions = TouchAction(driver)
actions.press(elements[0]).wait(3000).move_to(elements[3]).perform().release()

time.sleep(2)
driver.quit()
