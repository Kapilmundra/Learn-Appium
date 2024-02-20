import time
from appium import webdriver
# from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# appium_service = AppiumService()
# appium_service.start()
# print(appium_service.is_running)

# for setting up desired capabilities
desiredCap = dict(
    deviceName="Android",
    platformName="Android",
    browserName="Chrome",
    automationname="uiautomator2"
)

# for loading capability inside the UiAutomator2
capabilities_options = UiAutomator2Options().load_capabilities(desiredCap)

# invoke a driver
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

driver.get('http:google.com')
print(driver.title)
driver.find_element(by=AppiumBy.XPATH, value="//*[@name='q']").send_keys("Kapil")
time.sleep(2)
driver.press_keycode(66)
driver.quit()

# appium_service.stop()
