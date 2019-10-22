from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time, math, os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link="http://suninjuly.github.io/explicit_wait2.html"
    browser=webdriver.Chrome()
    browser.get(link)
    
    
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
        
    button=browser.find_element_by_id("book")
    button.click()

    browser.execute_script("window.scrollBy(0,350);")

    num=browser.find_element_by_id("input_value")
    pole=browser.find_element_by_css_selector('.form-control[id="answer"]')
    pole.send_keys(str(calc(num.text)))

    btn=browser.find_element_by_css_selector('button[id="solve"]')
    btn.click()
        
    
    # ждем загрузки страницы
    time.sleep(1)

        
finally:
    # успеваем скопировать код за 30 сек
    time.sleep(5)
    # закрываем браузер
    browser.quit()

