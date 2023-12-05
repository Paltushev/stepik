from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
# Open the webpage
url = "https://SunInJuly.github.io/execute_script.html"
driver = webdriver.Chrome()
driver.get(url)

try:
    # Read the value of variable x
    x_element = driver.find_element_by_id("input_value")
    x = int(x_element.text)

    # Calculate the mathematical function of x
    result = math.log(abs(12 * math.sin(x)))

    # Scroll the page down
    driver.execute_script("window.scrollBy(0, 100);")

    # Enter the answer in the text field
    answer_input = driver.find_element_by_id("answer")
    answer_input.send_keys(str(result))

    # Select the checkbox "I'm the robot"
    robot_checkbox = driver.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    # Toggle the radiobutton "Robots rule!"
    robot_radio = driver.find_element_by_id("robotsRule")
    robot_radio.click()

    # Click the "Submit" button
    submit_button = driver.find_element_by_css_selector("button[type='submit']")
    submit_button.click()

finally:
    # Пауза для визуальной проверки результата
    time.sleep(10)
    # Close the browser window after execution
    driver.quit()