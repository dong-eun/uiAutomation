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
    "automationName": "UiAutomator2"
}

url = "http://localhost:4723"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chrome")
el.click()
time.sleep(5)
wait = WebDriverWait(driver, 10)

searchBar = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='Search or type web address']")))
searchBar.send_keys("locat")

# driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Search or type web address']").send_keys("Lokesh")
