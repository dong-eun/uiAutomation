import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

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
driver.implicitly_wait(50)  # 암시적 대기 설정

# 'Continue' 버튼 찾기
continue_el = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')

# 'Continue' 버튼이 표시되면 클릭하고 다음 알림 대기
if continue_el.is_displayed():
    continue_el.click()
    wait = WebDriverWait(driver, 10)  # 명시적 대기 설정
    el1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
    el1.click()

# 명시적 대기와 무시할 예외 설정
wait1 = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

# 'Views' 항목이 나타날 때까지 대기하고 클릭
el2 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Views']")))
el2.click()

# 'Gallery' 항목이 나타날 때까지 대기하고 클릭
el3 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Gallery']")))
el3.click()

# '1. Photos' 항목이 나타날 때까지 대기하고 클릭
el4 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='1. Photos']")))
el4.click()

# W3C Actions API를 사용하여 수평 스크롤 동작을 구현
def perform_scroll(driver, start_el, end_el):
    actions = ActionBuilder(driver)
    touch = PointerInput(PointerInput.Kind.TOUCH, "finger")
    actions.add_action(
        touch.create_pointer_move(duration=0, x=start_el.rect['x'], y=start_el.rect['y'], origin='viewport')
    )
    actions.add_action(touch.create_pointer_down(PointerInput.MouseButton.LEFT))
    actions.add_action(
        touch.create_pointer_move(duration=1000, x=end_el.rect['x'], y=end_el.rect['y'], origin='viewport')
    )
    actions.add_action(touch.create_pointer_up(PointerInput.MouseButton.LEFT))
    actions.perform()

# 첫 번째 사진 요소 찾기
start_el = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
end_el = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[last()]")

# 앞으로 스크롤
perform_scroll(driver, start_el, end_el)

# 뒤로 스크롤 (시작과 끝 요소를 바꿔서 호출)
perform_scroll(driver, end_el, start_el)
