import time


class Utils:

    @staticmethod
    def pressKeysOnKeyboard(driver, keys):
        for key in keys:
            driver.press_keycode(key.value)
