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
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.google.android.apps.contacts.activities.PeopleActivity"
}

url = "http://localhost:4723"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Allow"]').click()

element = driver.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.google.android.contacts:id/cliv_name_textview"]')
print(len(element))

action = ActionChains(driver)

# 롱 프레스할 요소 선택
target_element = element[1]

action.w3c_actions.pointer_action.pointer_down(target_element).pause(2000).pointer_up().release()

action.w3c_actions.pointer_action.click_and_hold(target_element).pause(2).release()
action.perform()