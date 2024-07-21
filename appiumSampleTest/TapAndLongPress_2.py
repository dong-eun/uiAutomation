import time
from appium import webdriver
from typing import Any, Dict
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import Pause
from appium.options.common import AppiumOptions

cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.google.android.apps.contacts.activities.PeopleActivity"
}

url = "http://localhost:4723/wd/hub"

options = AppiumOptions()
options.load_capabilities(cap)

driver = webdriver.Remote(command_executor=url, options=options)
driver.implicitly_wait(50)

try:
    skip_elements = driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Skip"]')
    if skip_elements:
        skip_elements[0].click()
except Exception as e:
    print(f"An error occurred: {e}")

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Allow"]').click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ListView[@resource-id="android:id/list"]').click()

elements = driver.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.google.android.contacts:id/cliv_name_textview"]')
print(len(elements))

# 롱 프레스할 요소 선택
target_element = elements[0]

# W3C Actions API를 사용하여 요소 롱 프레스
finger = PointerInput(kind="touch", name="finger")
actions = ActionBuilder(driver, mouse=finger)

# W3C Actions를 사용하여 롱 프레스 동작 추가
actions.pointer_action.move_to(target_element).pointer_down().pause(2).pointer_up()

# 액션 실행
actions.perform()
