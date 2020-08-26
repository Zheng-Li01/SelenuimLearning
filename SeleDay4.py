from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# options  = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(10)
driver.get("https://www.baidu.com")
driver.execute_script('window.open()')
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.sohu.com/a/290128640_120050566')

driver.switch_to.window(driver.window_handles[0])
driver.get('https://www.cnblogs.com/songzhixue/p/11270593.html')

driver.close()
driver.quit()
# print(driver.get_cookies())
# driver.add_cookie({'name':'name', 'domain':'domain','value':'value'})
# print(driver.get_cookies())
# driver.delete_all_cookies()
# print(driver.get_cookies())
# driver.close()
    # driver.get("https://www.sohu.com/a/290128640_120050566")
    # driver.get("https://www.cnblogs.com/songzhixue/p/11270593.html")
    # driver.back()
    # time.sleep(1)
    # driver.forward()
    # driver.close()
    # WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('kw')).send_keys('lambda')

    # input_Data = driver.find_element_by_name('zu-top-add-question')
    # print(input_Data)

    # print(driver.title)
    # print(driver.name)
    # print(driver.find_element_by_id('setf').text)
    # print(driver.find_element_by_id('kw').tag_name)
    # print(driver.find_element_by_id('kw').get_attribute('class'))
    # print(driver.find_element_by_id('kw').get_property('class'))

    # driver.fullscreen_window()
    # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # driver.execute_script('alert("To Bottom")')
    # input_data = driver.find_element_by_id('kw')
    # input_data.send_keys('数据分析')
    # input_data.send_keys(Keys.ENTER)
    # input_data.clear()
    # wait = WebDriverWait(driver,10)
    # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # print(driver.current_url)
    # print(driver.get_cookies)
    # print(driver.page_source)
