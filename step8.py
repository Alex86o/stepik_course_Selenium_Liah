from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(" http://suninjuly.github.io/explicit_wait2.html")

# Ожидание пока кнопка станет активной в течении 5 секунд каждые 500мс
wait = WebDriverWait(browser,12)
price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

book = browser.find_element(By.ID, "book").click()

input2 = browser.find_element(By.ID, "input_value" )
x = input2.text

input3 = browser.find_element(By.ID, "answer")
input3.send_keys(calc(x))

input4 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
input4.click()

time.sleep(30)
browser.quit()