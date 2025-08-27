import time
import names
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FILL_DELAY   = 0.4
PAGE_DELAY   = 3

def slow_type(element, text, delay=0.08):
    """Simulasikan pengetikan manusia"""
    element.clear()
    for ch in text:
        element.send_keys(ch)
        time.sleep(delay)

def register(driver, email: str, password: str):
    """Isi form registrasi UpCloud"""
    driver.get("https://signup.upcloud.com/")
    wait = WebDriverWait(driver, 10)

    # first name
    fn = wait.until(EC.element_to_be_clickable((By.NAME, "first_name")))
    slow_type(fn, names.get_first_name())

    # last name
    ln = driver.find_element(By.NAME, "last_name")
    slow_type(ln, names.get_last_name())

    # email
    em = driver.find_element(By.NAME, "email")
    slow_type(em, email)

    # password
    pw = driver.find_element(By.NAME, "password")
    slow_type(pw, password)

    # confirm password
    cp = driver.find_element(By.NAME, "password_confirmation")
    slow_type(cp, password)

    # agree to terms
    checkbox = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    ActionChains(driver).move_to_element(checkbox).click().perform()

    # submit
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(PAGE_DELAY)

def authenticate(driver, code: str):
    """Isi kode verifikasi"""
    wait = WebDriverWait(driver, 10)
    otp = wait.until(EC.element_to_be_clickable((By.NAME, "verification_code")))
    slow_type(otp, code)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(PAGE_DELAY)
