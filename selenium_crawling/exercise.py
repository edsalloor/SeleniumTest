from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
import page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import MainPageLocators


class EspolCatalogSearch():
    fac_names = []
    car_names = []
    car_codes = []
    car_curris = []

    def test_exercise(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://www.espol.edu.ec/es/educacion/grado/catalogo")

        #Load the main page. In this case http://www.espol.edu.ec/es/educacion/grado/catalogo
        main_page = page.MainPage(self.driver)

        print("Crawling ESPOL careers catalog...")
        main_page.get_faculties_div()
        self.fac_names = main_page.faculties_names
        self.car_names = main_page.careers_names
        self.car_codes = main_page.careers_codes
        self.car_curris = main_page.careers_curriculum

        file_name = 'test_excercise.csv'
        with open('test_excercise.csv', mode='w', encoding='utf-8', newline='') as exercise_file:
            xrcs_writer = csv.writer(exercise_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            xrcs_writer.writerow(['career_name_en', 'career_code', 'faculty_name', 'link_to_career_curriculum'])

            for i in range(0, len(self.fac_names)):
                for j in range(0, len(self.car_names[i])):
                    xrcs_writer.writerow([self.car_names[i][j], self.car_codes[i][j], self.fac_names[i], self.car_curris[i][j]])

        exercise_file.close()
        self.driver.close()
        print("The file '"+ file_name + "' has been created")

    def bonus_exercise(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)  # seconds

        file_name = 'bonus_excercise.csv'
        with open('bonus_excercise.csv', mode='w', encoding='utf-8', newline='') as bonus_file:
            xrcs_writer = csv.writer(bonus_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            xrcs_writer.writerow(['elective_subject_code', 'elective_subject_name_en'])

            for i in range(0, len(self.fac_names)):
                for j in range(0, len(self.car_curris[i])):
                    self.driver.get(self.car_curris[i][j])

                    print("Reading elective courses of " + self.car_names[i][j] + "...")
                    xrcs_writer.writerow([])
                    xrcs_writer.writerow(['--------------- '+self.car_names[i][j]+' ---------------'])
                    xrcs_writer.writerow([])

                    cur_page = page.MainPage(self.driver)       # Load the curriculum page of each career
                    cur_page.click_elective_subject()           # Click on elective courses to display the subjects
                    WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(MainPageLocators.LEN_SELECTOR))
                    cur_page.click_len_rows_selector()          # Select the max length of visible rows
                    WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "tbl_materias_complementarias")))
                    elec_sub_dic = cur_page.get_elective_subjects()     #Reading elements

                    for k,v in elec_sub_dic.items():
                        print(k,v)
                        xrcs_writer.writerow([k, v])

        bonus_file.close()
        self.driver.close()
        print("The file '" + file_name + "' has been created")


if __name__ == "__main__":
    search = EspolCatalogSearch()
    search.test_exercise()
    search.bonus_exercise()