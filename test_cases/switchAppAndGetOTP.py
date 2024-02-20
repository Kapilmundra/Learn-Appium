import time

from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from utils.enum import KeyCodeNumber
from utils.utils import Utils

appium_service = AppiumService()
appium_service.start()
desired_cap = dict(
    deviceName="Android",
    platformName="Android",
    appPackage="net.one97.paytm",
    appActivity="net.one97.paytm.landingpage.activity.AJRMainActivity",
    automationname="uiautomator2"
)

capability_options = UiAutomator2Options().load_capabilities(desired_cap)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capability_options)
driver.implicitly_wait(5)

try:
    driver.find_element(by=AppiumBy.ID, value='com.google.android.gms:id/cancel').click()

    # driver.find_element(by=AppiumBy.ID, value='net.one97.paytm:id/et_registered_mobile').click()
    # Utils.pressKeysOnKeyboard(
    #     driver=driver,
    #     keys=[
    #         KeyCodeNumber.KEYCODE_8,
    #         KeyCodeNumber.KEYCODE_9,
    #         KeyCodeNumber.KEYCODE_5,
    #         KeyCodeNumber.KEYCODE_5,
    #         KeyCodeNumber.KEYCODE_2,
    #         KeyCodeNumber.KEYCODE_9,
    #         KeyCodeNumber.KEYCODE_6,
    #         KeyCodeNumber.KEYCODE_7,
    #         KeyCodeNumber.KEYCODE_4,
    #         KeyCodeNumber.KEYCODE_9,
    #     ]
    # )
    # driver.hide_keyboard()
    #
    # driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Proceed Securely"]').click()
    #
    # driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button').click()
    # driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button').click()
    # driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id'
    #                                           '/permission_allow_foreground_only_button').click()

    # driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Forgot Password?']").click()
    # driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Proceed Securely"]').click()

    print("1")
    intent = {
        'intent': 'android.intent.action.MAIN',
        'appPackage': 'com.google.android.apps.messaging',
        'appActivity': 'com.google.android.apps.messaging.ui.ConversationListActivity'
    }
    driver.execute_script('mobile:startActivity', intent)

    # driver.start_activity("com.google.android.apps.messaging", "com.google.android.apps.messaging.ui"
    #                                                            ".ConversationListActivity")
    print("2")

    driver.find_element(by=AppiumBy.ID, value='com.google.android.apps.messaging:id/swipeableContainer')[0].click()
    messages = driver.find_element(by=AppiumBy.ID, value='com.google.android.apps.messaging:id/message_text')

    print(messages[-1].text)


except Exception as e:
    print(e)

driver.quit()
appium_service.stop()
