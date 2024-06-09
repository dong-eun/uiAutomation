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
    "appPackage": "com.google.android.dialer",
    "appActivity": "com.android.dialer.main.impl.MainActivity"
}

url = "http://localhost:4723"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Recents']").click()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='key pad').click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="1,"]').click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="1,"]').click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="5,JKL"]').click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="dial"]').click()

time.sleep(3)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="End call"]').click()