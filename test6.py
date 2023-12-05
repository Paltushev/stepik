from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Создаем объект драйвера (браузера)
driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver и путь к нему добавлен в системную переменную PATH

try:
    # Открываем страницу
    driver.get("https://suninjuly.github.io/selects1.html")

    # Находим элементы с числами
    num1_element = driver.find_element(By.ID, "num1")
    num2_element = driver.find_element(By.ID, "num2")

    # Получаем текстовое содержимое элементов и вычисляем сумму чисел
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    sum_result = num1 + num2

    # Находим выпадающий список и выбираем значение, равное расчетной сумме
    select_element = Select(driver.find_element(By.TAG_NAME, "select"))
    select_element.select_by_value(str(sum_result))

    # Нажимаем кнопку "Submit"
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    # Пауза для визуальной проверки результата
    time.sleep(10)
    # Закрываем браузер после выполнения действий
    driver.quit()