from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

# Инициализация веб-драйвера
browser = webdriver.Chrome()  # Укажите свой путь к драйверу, если используете другой браузер
browser.implicitly_wait(5)  # Неявное ожидание для поиска элементов

# Открытие страницы
url = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(url)

try:
    # Дождаться, когда цена дома уменьшится до $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажатие на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Получение значения для решения капчи
    x_value = int(browser.find_element(By.ID, "input_value").text)

    # Решение математической задачи
    answer = str(math.log(abs(12 * math.sin(x_value))))

    # Ввод ответа в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # Отправка заполненной формы
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Для демонстрации результата
    input("Press Enter to close the browser...")
    browser.quit()