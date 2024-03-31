import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
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

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID)))

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Allow"]').click()

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create contact")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"First name\"]")
el2.send_keys("Dominic001")
el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Last name\"]")
el3.send_keys("Kim")
el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Phone\"]")
el4.send_keys("+821099601100")
el5 = driver.find_element(by=AppiumBy.ID, value="com.google.android.contacts:id/toolbar_button")
el5.click()