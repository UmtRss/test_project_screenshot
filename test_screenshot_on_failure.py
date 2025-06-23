from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def test_screenshot_on_failure():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("hatalikullanici")
    driver.find_element(By.ID, "password").send_keys("hatalisifre")
    driver.find_element(By.CSS_SELECTOR, ".radius").click()

    error_msg = driver.find_element(By.ID, "flash").text

    try:
        assert "Welcome" in error_msg
    except AssertionError:
        # Klasör yoksa oluştur
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/login_fail.png")
        raise

    driver.quit()
