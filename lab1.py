import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


def read_x():
    driver.get('http://suninjuly.github.io/math.html')
    x_text = driver.find_element(By.ID, 'input_value').text
    return int(x_text)


def count_formula(value):
    return math.log(math.fabs(12 * math.sin(value)))


def write_answer(answer):
    driver.find_element(By.ID, 'answer').send_keys(answer)


def mark_checkbox():
    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    checkbox.click()


def robots_rule():
    button = driver.find_element(By.ID, 'robotsRule')
    button.click()


def submit():
    submit_button = driver.find_element(By.XPATH, '/html/body/div/form/button')
    submit_button.click()


def run_lab_1():
    x = read_x()
    result = count_formula(x)
    write_answer(result)
    mark_checkbox()
    robots_rule()
    submit()
