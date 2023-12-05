from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

# Инициализация веб-драйвера
browser = webdriver.Chrome()  # Укажите свой путь к драйверу, если используете другой браузер
browser.implicitly_wait(5)  # Неявное ожидание для поиска элементов

# Открытие страницы
url = "http://suninjuly.github.io/alert_accept.html"
browser.get(url)

try:
    # Находим кнопку и кликаем на нее
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Принятие confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # Получение значения для решения капчи
    x_value = int(browser.find_element(By.ID, "input_value").text)

    # Решение математической задачи
    answer = str(math.log(abs(12 * math.sin(x_value))))

    # Ввод ответа в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # Отправка заполненной формы
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    # Пауза для просмотра результата перед закрытием окна
    input("Press Enter to close the browser...")
    browser.quit()