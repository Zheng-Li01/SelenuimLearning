from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=chrome_options)

class PythonOrgSearch(unittest.TestCase):
    # driver = webdriver.Chrome(options=chrome_options)
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.ENTER)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ =="__main__":
    unittest.main()

# driver.get("http://www.python.org")
# assert "Python" in driver.title

# elem = driver.find_element_by_name("q")
# # elem = driver.find_element_by_id("id-search-field")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# # print(driver.page_source)
# # driver.close()