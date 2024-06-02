import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput


cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.socialnmobile.dictapps.notepad.color.note",
    "appActivity": "com.socialnmobile.colornote.activity.Main",
    "language": "en"
}

url = "http://localhost:4723"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

try:
    step_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="NEXT"]')
    step_button.click()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    step_button_2 = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="NEXT"]')
    step_button_2.click()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    allow_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Allow"]')
    allow_button.click()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    skip_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="SKIP"]')
    skip_button.click()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    menu = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="More"]')
    menu.click()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    facebook = driver.find_element(AppiumBy.XPATH, '//android.widget.GridView[@resource-id="com.socialnmobile.dictapps.notepad.color.note:id/more_grid"]/android.widget.LinearLayout[6]')
    facebook.click()
except Exception as e:
    print(f"An error occurred: {e}")

print(driver.context)
print(driver.contexts)

try:
    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Log in"]')))
    print(wait.text)
except Exception as e:
    print(f"An error occurred: {e}")

