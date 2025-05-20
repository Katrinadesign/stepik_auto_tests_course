# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.CLASS_NAME, "first")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.CLASS_NAME, "second")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "third")
#     input3.send_keys("Ram@mail.ru")
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     button.click()
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#
#     input1 = browser.find_element(By.ID, "answer")
#     y = calc(x)
#     input1.send_keys(y)
#
#     input2 = browser.find_element(By.ID, "robotCheckbox")
#     input2.click()
#     input3 = browser.find_element(By.ID, "robotsRule")
#     input3.click()
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#     x_element = browser.find_element(By.ID, "treasure")
#     x = x_element.get_attribute("valuex")
#     y = calc(x)
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#     input2 = browser.find_element(By.ID, "robotCheckbox")
#     input2.click()
#     input3 = browser.find_element(By.ID, "robotsRule")
#     input3.click()
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
# from selenium.webdriver.support.ui import Select
#
#
# try:
#     link = "https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x = browser.find_element(By.ID, "num1").text
#     y = browser.find_element(By.ID, "num2").text
#
#     z = str(int(x) + int(y))
#
#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(z)
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# time.sleep(10)
# browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# try:
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x = browser.find_element(By.ID, "input_value").text
#     y = str(math.log(abs(12*math.sin(int(x)))))
#
#     browser.execute_script("window.scrollBy(0, 150)", "")
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#     input2 = browser.find_element(By.ID, "robotCheckbox")
#     input2.click()
#     input3 = browser.find_element(By.ID, "robotsRule")
#     input3.click()
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import os
#
# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(current_dir, 'test.txt')
#
# with open(file_path, 'w') as f:
#     f.write('automationbypython')
#
# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.XPATH, "//*[@name='firstname']")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.XPATH, "//*[@name='lastname']")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, "//*[@name='email']")
#     input3.send_keys("Ram@mail.ru")
#
#     element = browser.find_element(By.ID, "file")
#     element.send_keys(file_path)
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(20)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     x = browser.find_element(By.ID, "input_value").text
#     y = str(math.log(abs(12*math.sin(int(x)))))
#
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     x = browser.find_element(By.ID, "input_value").text
#     y = str(math.log(abs(12*math.sin(int(x)))))
#
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# import math
#
#
# try:
#     link = "http://suninjuly.github.io/explicit_wait2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
#     button1 = browser.find_element(By.ID, "book")
#     button1.click()
#
#     browser.execute_script("window.scrollBy(0, 150)", "")
#
#     x = browser.find_element(By.ID, "input_value").text
#     y = str(math.log(abs(12*math.sin(int(x)))))
#
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#     button = browser.find_element(By.XPATH, "//*[@type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

