import unittest
from selenium import webdriver
import time


class PythonJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_job(self):
        driver = self.driver
        driver.get("http://www.python.org")
        time.sleep(4)
        job = driver.find_element_by_css_selector('#top > nav > ul > li.jobs-meta > a')
        job.click()
        time.sleep(4)
        locations = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div/ol/li/h2/span[2]')
        res_location = ''
        for location in locations:
            res_location += location.text + '\n'
        print(res_location)
        self.assertIn('Czech Republic', res_location)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
