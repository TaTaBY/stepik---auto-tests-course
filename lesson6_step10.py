from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector ("div.first_block div.form-group.first_class input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector ("div.first_block div.form-group.second_class input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector ("div.first_block div.form-group.third_class input")
    input3.send_keys("test@test.test")
    input4 = browser.find_element_by_css_selector ("div.second_block div.form-group.first_class input")
    input4.send_keys("80293337777")
    input5 = browser.find_element_by_css_selector ("div.second_block div.form-group.second_class input")
    input5.send_keys("Russia")
    button = browser.find_element_by_xpath  ("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла