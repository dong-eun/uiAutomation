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
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.android.contacts.activities.PeopleActivity",
    "language": "en"
}

url = "http://localhost:4723"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

try:
    skip_button = driver.find_element(AppiumBy.XPATH, value='//android.widget.Button[@text="Skip"]')
    skip_button.click()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    allow_button = driver.find_element(AppiumBy.XPATH, value='//android.widget.Button[@text="Allow"]')
    allow_button.click()
except Exception as e:
    print(f"An error occurred: {e}")

ele_setting = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Create contact')
ele_setting.click()

spinner_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Mobile")')
spinner_button.click()
