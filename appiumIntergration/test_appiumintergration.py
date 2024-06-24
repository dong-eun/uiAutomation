from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException


def setup_function(function):
    global driver
    global appium_service
    appium_service = AppiumService()
    appium_options = AppiumOptions()
    appium_service.start()
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "platformVersion": "13.0",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "appPackage": "com.hmh.api",
        "appActivity": ".ApiDemos"
    }

    url = "http://127.0.0.1:4723"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))


def teardown_function():
    driver.quit()
    appium_service.stop()


def test_demo1():
    print("Demo pytest")
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
        driver.find_element(AppiumBy.XPATH,
                            '//android.widget.Button[@resource-id="com.hmh.api:id/two_buttons"]').click()
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert_message = alert.text
        print(f"alert message : {alert_message}")
        alert.accept()
    except Exception as e:
        print(f"An error occurred: {e}")

