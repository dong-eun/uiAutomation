import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.google.android.apps.contacts.activities.PeopleActivity"
}

url = "http://localhost:4723"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

skip_element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Skip"]')

if skip_element:
    skip_element.click()
else:
    pass

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Allow"]').click()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Create contact').click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="First name"]').send_keys("Dominic02")

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Last name"]').send_keys("Jun")

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]').send_keys("01099001100")

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Save"]').click()