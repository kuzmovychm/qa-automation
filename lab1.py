import time
from SeleniumHelper import *

driver = webdriver.Chrome(ChromeDriverManager().install())


def mark_checkbox():
    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    checkbox.click()


def robots_rule():
    button = driver.find_element(By.ID, 'robotsRule')
    button.click()


if __name__ == '__main__':
    driver.get('http://suninjuly.github.io/math.html')
    x = read_int(driver, (By.ID, 'input_value'))
    result = count_common_formula(x)
    write_to_element(driver, (By.ID, 'answer'), result)
    mark_checkbox()
    robots_rule()
    click(driver, (By.XPATH, '/html/body/div/form/button'))
    time.sleep(3)
