from selenium import webdriver

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
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
print(driver.title)

