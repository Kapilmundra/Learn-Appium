import time
from pathlib import Path
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()
appium_service.start()

try:
    desired_cap = {
        'platformName': 'Android',
        'deviceName': 'Android',
        # 'appPackage': 'in.amazon.mShop.android.shopping',
        # 'appActivity': 'com.amazon.twa.CustomTWALaunncherActivity'
        'app': str(Path().absolute().parent) + '/app/amazon.apk'
    }
    # desired_cap['app'] = str(Path().absolute().parent)+'\\app\\amazon.apk'
    capability_option = UiAutomator2Options().load_capabilities(desired_cap)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capability_option)
    driver.implicitly_wait(5)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Continue in English').click()
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Skip sign in")').click()
    driver.find_element(by=AppiumBy.ID, value='in.amazon.mShop.android.shopping:id/skip_sign_in_button').click()
    driver.find_element(by=AppiumBy.ID, value='in.amazon.mShop.android.shopping:id/rs_search_src_text').click()
    # Explicit wait
    # wait = WebDriverWait(driver,10)
    # wait.until(EC.element_to_be_clickable((By.ID,'in.amazon.mShop.android.shopping:id/rs_search_src_text')))
    driver.find_element(by=AppiumBy.ID, value='in.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys('Shoes')
    driver.press_keycode(66)
    time.sleep(5)
    driver.quit()
except Exception as e:
    print(e)

appium_service.stop()
