import time
from pathlib import Path
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from test_cases.scroll_util import ScrollUtil
from appium.options.android import UiAutomator2Options

desired_caps = {'platformName': 'Android', 'deviceName': 'Android', 'appPackage': 'com.android.contacts',
                'appActivity': 'com.android.contacts.DialtactsContactsEntryActivity'}
capability_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', options=capability_options)
driver.implicitly_wait(5)

ScrollUtil.scrollToTextByAndroidUIAutomator("Akash", driver);

ScrollUtil.swipeUp(4, driver)
ScrollUtil.swipeDown(4, driver)

elements = driver.find_elements(by=AppiumBy.ID, value='com.android.contacts:id/cliv_name_textview')
print(len(elements))


actions = TouchAction(driver)
# actions.tap(elements[2])
actions.long_press(elements[2])
actions.perform()

time.sleep(3)


# Use Ui scrollable class to implement this
# UiScrollable -> constructor UiSelector -> calling scrollable function up to first instance(value) appear
# -> scrollIntoView -> constructor UiSelector -> calling textContains up to first instance(value) appear
'''
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                    value="new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new "
                          "UiSelector().textContains('Akash').instance(0))").click()
'''

'''
driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(
0)).scrollIntoView(new UiSelector().textContains("Akash").instance(0))').click()
'''


# swipe up -> start_x -> 514, start_y -> 600, end_x -> 514, end_y -> 200 duration -> 1000 (end_y < start_y)
# swipe down -> start_x -> 514, start_y -> 500, end_x -> 514, end_y -> 800 duration -> 1000 (end_y > start_y)
'''
driver.swipe(514, 600, 514, 200, 1000)
driver.swipe(514, 600, 514, 200, 1000)
driver.swipe(514, 600, 514, 200, 1000)
driver.swipe(514, 600, 514, 200, 1000)

driver.swipe(514, 500, 514, 800, 1000)
driver.swipe(514, 500, 514, 800, 1000)
driver.swipe(514, 500, 514, 800, 1000)
driver.swipe(514, 500, 514, 800, 1000)
'''

