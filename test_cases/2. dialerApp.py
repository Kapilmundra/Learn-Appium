# from importlib.resources import path
# from pathlib import Path
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

appiumService = AppiumService()
appiumService.start()

try:
    desiredCap = dict(
        deviceName="Android",
        platformName="Android",
        appPackage="com.google.android.dialer",
        appActivity="com.google.android.dialer.extensions.GoogleDialtactsActivity",
        automationname='uiautomator2'
        # app=str(Path().absolute().parent) + '/app/amazon.apk'
    )

    capability_option = UiAutomator2Options().load_capabilities(desiredCap)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capability_option)

    driver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/dialpad_fab").click()
    driver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/one").click()
    driver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/two").click()
    driver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/three").click()
    driver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/four").click()
    driver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/dialpad_voice_call_button").click()
    driver.quit()
except Exception as e:
    print(e)

appiumService.stop()
print(appiumService.is_running)
