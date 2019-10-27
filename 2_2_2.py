from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects1"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    select = Select(browser.find_element_by_tag_name("select"))
    x = browser.find_element_by_id("num1")
    x = int(x.text)
    y = browser.find_element_by_id("num2")
    y = int(y.text)

    z = x + y
   
    select.select_by_value(str(z))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла