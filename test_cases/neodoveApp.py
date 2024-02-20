import time
from pathlib import Path

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desiredCap = dict(
    deviceName="Android",
    platformName="Android",
    # appPackage = "com.cellphone.neodove",
    # appActivity = ".MainActivity",
    app=str(Path().absolute().parent) + "/app/neodove-flutter-staging.apk"
)

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desiredCap)
driver.implicitly_wait(5)
time.sleep(3)

driver.find_element(by=AppiumBy.CSS_SELECTOR, value="android.widget.Button[content-desc='Sign In']").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login using Password").click()
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[1]").send_keys("998877")
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[2]").send_keys("12345")


driver.quit()
