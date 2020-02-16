from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    #Locator for catalog page
    FACULTY_DIV = (By.XPATH, "//div[starts-with(@id,'headingF')]/..")

    #Locators for curriculum page
    ELECTIVE_COURSE_A = (By.XPATH, "//p[@id='informacion']/a[.='Elective course']")
    SUBJECT_TR = (By.XPATH, "//table[@id='tbl_materias_complementarias']/tbody/tr")

    #Location for elective subject tables
    PAGE_BUTTONS = (By.XPATH,"//div[@id='tbl_materias_complementarias_paginate']/ul/li[position() >1 and position()< last()]")

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    FACULTY_STRONG = (By.XPATH, ".//strong")
    FACULTY_LI = (By.XPATH, ".//strong[contains(text(),'Undergraduate Programs')]/following::ul[1]//li")
    LINK = (By.XPATH, ".//a")

    #Locators relative to SUBJECT_TR
    SUBJECT_TD1 = (By.XPATH, "./td[1]")
    SUBJECT_TD2 = (By.XPATH, "./td[2]")

    #Locators relative to PAGE_BUTTONS