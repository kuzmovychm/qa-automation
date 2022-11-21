import time
import math
from SeleniumHelper import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


def book():
    book_button = driver.find_element(By.ID, 'book')
    book_button.click()


if __name__ == '__main__':
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    book()
    x = read_int(driver, (By.ID, 'input_value'))
    result = count_common_formula(x)
    write_to_element((By.ID, 'answer'), result)
    click((By.ID, 'solve'))
