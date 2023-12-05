from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Открытие страницы
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Поиск элемента-картинки и получение значения атрибута valuex
treasure = browser.find_element(By.ID, "treasure")
x = treasure.get_attribute("valuex")

# Вычисление математической функции от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

# Ввод ответа в текстовое поле
input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(y)

# Отметка checkbox "I'm the robot"
checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

# Выбор radiobutton "Robots rule!"
radiobutton = browser.find_element(By.ID, "robotsRule")
radiobutton.click()

# Нажатие на кнопку "Submit"
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Пауза для визуальной проверки результата
time.sleep(5)

# Закрытие браузера
browser.quit()