import unittest
import time
import uuid

from SeleniumHelper import write_to_element, click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class LabTestCase(unittest.TestCase):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_warranty_search(self):
        self.driver.get('http://demo-store.seleniumacademy.com/')
        search_form = self.driver.find_element(By.ID, 'search_mini_form')
        search_form.find_element(By.TAG_NAME, 'input').send_keys('warranty')
        search_form.find_element(By.TAG_NAME, 'button').click()
        grid = self.driver.find_element(By.CLASS_NAME, 'products-grid')
        items_count = len(grid.find_elements(By.CLASS_NAME, 'item'))
        self.assertEqual(items_count, 2)

    def test_registration(self):
        self.driver.get('http://demo-store.seleniumacademy.com/customer/account/create/')
        write_to_element(self.driver, (By.ID, 'firstname'), 'Max')
        write_to_element(self.driver, (By.ID, 'lastname'), 'Kuz')
        write_to_element(self.driver, (By.ID, 'email_address'), str(uuid.uuid1()) + '@mail.com')
        write_to_element(self.driver, (By.ID, 'password'), 'qweRty98@')
        write_to_element(self.driver, (By.ID, 'confirmation'), 'qweRty98@')
        register_button = self.driver.find_element(By.CLASS_NAME, 'buttons-set').find_element(By.TAG_NAME, 'button')
        register_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_matches('.+\/customer\/account\/index\/'))
        success_text = self.driver.find_element(By.CLASS_NAME, 'success-msg').find_element(By.TAG_NAME, 'span').text
        self.assertEqual(self.driver.current_url, 'http://demo-store.seleniumacademy.com/customer/account/index/')
        self.assertEqual(success_text, 'Thank you for registering with Madison Island.')

    def test_language_change(self):
        self.driver.get('http://demo-store.seleniumacademy.com')
        selector = self.driver.find_element(By.ID, 'select-language')
        options = selector.find_elements(By.TAG_NAME, 'option')
        for option in options:
            if option.text == 'German':
                option.click()
        WebDriverWait(self.driver, 10).until(EC.url_matches('.+___store=german.+'))
        self.assertEqual(self.driver.current_url,
                         'http://demo-store.seleniumacademy.com/?___store=german&___from_store=default')


if __name__ == '__main__':
    unittest.main()
