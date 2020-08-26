from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)

class MainPageLocators(object):
    """
    A classs for main page locators,all main page locators shold come here
    """
    GO_BUTTON =(By.ID, "submit")

class SearchResultsPageLocators(object):
    """A class for search results locators,all search results locators should come here"""
    pass