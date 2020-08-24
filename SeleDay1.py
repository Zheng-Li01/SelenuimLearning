from selenium import webdriver
import time

# option = webdriver.ChromeOptions()
# option.add_argument("disable-infobars")
# driver = webdriver.Chrome(chrome_options=option)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://blog.csdn.net/github_37216944/article/details/79053781")
# print(driver.title)

driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
# driver.get("https://kyfw.12306.cn/otn/")
# print(driver.title)
# driver.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]").click()
# driver.find_element_by_id("J-userName").send_keys("xxxx")
# driver.find_element_by_id("J-password").send_keys("xxx")
# time.sleep(10)

# driver.find_element_by_css_selector('//*[@id="pop_159825583505098955"]/div[2]/div[3]/a').click()
# time.sleep(5)

# element = driver.find_element_by_xpath('//*[@id="J-index"]/a')
# driver.execute_script("arguments[0].click();", element)
# time.sleep(5)

driver.get("https://www.12306.cn/index/index.html")
time.sleep(2)
driver.find_element_by_id("fromStationText").clear()
driver.find_element_by_id("fromStationText").send_keys(u"广州")
time.sleep(5)

element1 =driver.find_element_by_id("toStationText")
driver.execute_script("arguments[0].click();", element1)
driver.find_element_by_id("toStationText").send_keys(u"西安")
driver.send_keys("Enter")
time.sleep(5)

element2 = driver.find_element_by_id("search_one")
driver.execute_script("arguments[0].click();", element2)
time.sleep(2)




