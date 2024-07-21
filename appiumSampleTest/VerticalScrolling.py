import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

# 설정된 capabilities로 Appium 설정
cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.hmh.api",
    "appActivity": ".ApiDemos"
}

# Appium 서버 URL
url = "http://localhost:4723"

# WebDriver 인스턴스 생성 및 설정 로드
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)  # 암시적 대기

# 'Continue' 버튼 찾기
continue_el = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')

# 'Continue' 버튼이 표시되면 클릭하고 다음 알림 대기
if continue_el.is_displayed():
    continue_el.click()
    wait = WebDriverWait(driver, 10)  # 명시적 대기
    el1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
    el1.click()

# 명시적 대기와 무시할 예외 설정
wait1 = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

# 'App' 항목이 나타날 때까지 대기하고 클릭
el2 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='App']")))
el2.click()

# 'Activity' 항목이 나타날 때까지 대기하고 클릭
el3 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Activity']")))
el3.click()

# 수직 스크롤 가능한 목록을 끝까지 스크롤
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')

# 수직 스크롤 가능한 목록을 처음까지 스크롤
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(5)')

# deviceSize = driver.get_window_size()
# print(deviceSize)
#
# screenWidth = deviceSize['width']
# screenHeight = deviceSize['height']
# print(screenHeight)
# print(screenWidth)
#
# startX = screenWidth/2
# endX = screenWidth/2
# startY = screenHeight*8/9
# endY = screenHeight/9
#
# actions = TouchAction(driver)