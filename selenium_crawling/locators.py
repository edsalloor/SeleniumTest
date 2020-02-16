from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    #Locator for catalog page
    FACULTY_DIV = (By.XPATH, "//div[starts-with(@id,'headingF')]/..")

    #Locators for curriculum page

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    FACULTY_STRONG = (By.XPATH, ".//strong")
    FACULTY_LI = (By.XPATH, ".//strong[contains(text(),'Undergraduate Programs')]/following::ul[1]//li")
    LINK = (By.XPATH, ".//a")