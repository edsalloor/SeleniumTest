from element import BasePageElement
from locators import MainPageLocators, SearchResultsPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    # Declares arrays that will contain the retrieved values
    faculties_names = []
    careers_names = []
    careers_codes = []
    careers_curriculum = []

    def get_faculties_div(self):
        faculties_div = self.driver.find_elements(*MainPageLocators.FACULTY_DIV)    #Main div for each faculty

        for fac_div in faculties_div:

            #Extract faculties names
            fac_strong = fac_div.find_element(*SearchResultsPageLocators.FACULTY_STRONG)
            fac_name = fac_strong.text.split("\n")[1]
            self.faculties_names.append(fac_name)

            #Getting the li for each career of the faculty
            fac_lis = fac_div.find_elements(*SearchResultsPageLocators.FACULTY_LI)
            names = []
            codes = []
            curriculums = []

            #Extracting career information of each li
            for li in fac_lis:
                career_txt = li.get_attribute("textContent")    #String that contains the name and code of the career

                career_name = career_txt[:career_txt.index("(")].strip()
                names.append(career_name)

                career_code = career_txt[career_txt.index(")")+1:].strip()
                codes.append(career_code)

                career_a = li.find_element(*SearchResultsPageLocators.LINK)
                curriculum_link = career_a.get_attribute("href")
                curriculums.append(curriculum_link)

                #print(career_name + ": " + career_code + "; " + curriculum_link)

            self.careers_names.append(names)
            self.careers_codes.append(codes)
            self.careers_curriculum.append(curriculums)

    def click_elective_subject(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.ELECTIVE_COURSE_A)
        element.click()

    def get_elective_subjects(self):
        subject_dic = {}
        subjects_tr = self.driver.find_elements(*MainPageLocators.SUBJECT_TR)

        for tr in subjects_tr:
            try:
                td1 = tr.find_element(*SearchResultsPageLocators.SUBJECT_TD1)
                td2 = tr.find_element(*SearchResultsPageLocators.SUBJECT_TD2)
                code = td1.get_attribute("textContent").strip()
                name = td2.get_attribute("textContent").strip()
                subject_dic[code] = name
            except:
                print("\033[93mSome elective subjects may have not been obtained...\033[0m")
        return subject_dic

