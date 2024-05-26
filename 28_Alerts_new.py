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
    "appPackage": "com.hmh.api",
    "appActivity": ".ApiDemos",
    "language": "en"
}

url = "http://localhost:4723"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

try:
    continue_element = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')
    continue_element.click()
except NoSuchElementException:
    print("Continue button not found.")
try:
    ok_element = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')
    ok_element.click()
except NoSuchElementException:
    print("OK button not found.")

driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="App"]').click()
driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Alert Dialogs"]').click()

try:
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.hmh.api:id/two_buttons"]').click()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_message = alert.text
    print(f"alert message : {alert_message}")
    alert.accept()
except Exception as e:
    print(f"An error occurred: {e}")

# alert = driver.switch_to.alert
# alert.accept()