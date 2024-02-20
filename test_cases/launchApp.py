import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desiredCap = dict(
    deviceName="Android",
    platformName="Android",
    appPackage="com.cellphone.neodove",
    appActivity="com.cellphone.neodove.MainActivity"
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desiredCap)

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SomeAccessibilityID")

time.sleep(5)

driver.quit()
