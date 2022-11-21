import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def read_int(driver: webdriver.Chrome, locator):
    text = driver.find_element(*locator).text
    return int(text)


def count_common_formula(x):
    return math.log(math.fabs(12 * math.sin(x)))


def write_to_element(driver: webdriver.Chrome, locator, value):
    driver.find_element(*locator).send_keys(value)


def click(driver: webdriver.Chrome, locator):
    driver.find_element(*locator).click()
