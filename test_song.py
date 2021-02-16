import unittest
from selenium import webdriver
import time



class TestAmalgama(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_song(self):
        driver = self.driver
        driver.get('https://www.amalgama-lab.com')
        time.sleep(7)
        element = driver.find_element_by_xpath('//*[@id="az_nav"]/ul/li[11]/a')
        time.sleep(4)
        element.click()
        time.sleep(5)
        element = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[2]/div[3]/ul/li[73]/div/div/a')
        element.click()
        time.sleep(5)
        element = driver.find_element_by_xpath('//*[@id="songs_nav"]/ul/ul/li[71]/a')
        element.click()
        time.sleep(5)
        original = driver.find_elements_by_class_name('original')
        translate = driver.find_elements_by_class_name('translate')
        original_text = ''
        translate_text = ''
        for texts in original:
            original_text += texts.text + '\n'
        for texts in translate:
            translate_text += texts.text + '\n'
        print(original_text, translate_text)
        self.assertIn('highway to hell', original_text)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
