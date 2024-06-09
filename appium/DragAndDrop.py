import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
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
    "appPackage": "com.mobeta.android.demodslv",
    "appActivity": ".Launcher",
    "language": "en"
}

url = "http://localhost:4723"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

continue_element = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')

try:
    if continue_element:
        continue_element.click()
except:
    pass

pop_element = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')

try:
    if pop_element:
        pop_element.click()
except:
    pass

driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Basic usage playground"]').click()

element = driver.find_elements(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.mobeta.android.demodslv:id/drag_handle"]')

action = ActionChains(driver)

target_element = element[0]

action.w3c_actions.pointer_action.click_and_hold(target_element).pause(3).move_to(element[5]).release()
action.perform()