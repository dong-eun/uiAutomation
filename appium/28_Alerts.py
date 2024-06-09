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
    "appPackage": "com.touchboarder.android.api.demos",
    "appActivity": "com.touchboarder.androidapidemos.MainActivity",
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

pop_element01 = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')

try:
    if pop_element01:
        pop_element01.click()
except:
    pass

pop_element02 = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="OK"]').click()


API_Demos = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="API Demos"]').click()
app_element = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="App"]').click()
alerts_dialogs = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Alert Dialogs"]').click()
long_message_alert = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK CANCEL DIALOG WITH A MESSAGE"]').click()

time.sleep(1)

# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

# driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()

alert_message = driver.switch_to.alert
text = alert_message.text

print(f"Alert text : {text}")