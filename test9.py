from selenium import webdriver
import math
import time

# Инициализация веб-драйвера
browser = webdriver.Chrome()  # Укажите свой путь к драйверу, если используете другой браузер

# Открытие страницы
url = "http://suninjuly.github.io/redirect_accept.html"
browser.get(url)

try:
    # Нажатие на кнопку
    button = browser.find_element("css selector", "button.trollface")
    button.click()

    # Переключение на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Получение значения для решения капчи
    x_value = browser.find_element("id", "input_value").text
    x_value = int(x_value)

    # Решение математической задачи
    answer = str(math.log(abs(12 * math.sin(x_value))))

    # Ввод ответа в текстовое поле
    answer_input = browser.find_element("id", "answer")
    answer_input.send_keys(answer)

    # Отправка заполненной формы
    submit_button = browser.find_element("css selector", "button[type='submit']")
    submit_button.click()

finally:
    # Для демонстрации результата
    time.sleep(5)
    browser.quit()