from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
import page

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

        main_page.get_faculties_div()
        fac_names = main_page.faculties_names
        car_names = main_page.careers_names
        car_codes = main_page.careers_codes
        car_curris = main_page.careers_curriculum

        file_name = 'test_excercise.csv'
        with open('test_excercise.csv', mode='w', encoding='utf-8', newline='') as exercise_file:
            xrcs_writer = csv.writer(exercise_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            xrcs_writer.writerow(['career_name_en', 'career_code', 'faculty_name', 'link_to_career_curriculum'])

            for i in range(0, len(fac_names)):
                for j in range(0, len(car_names[i])):
                    xrcs_writer.writerow([car_names[i][j], car_codes[i][j], fac_names[i], car_curris[i][j]])

        exercise_file.close()
        self.driver.close()
        print("The file '"+ file_name + "' has been created")

"""
        for i in range(0, len(fac_names)):
            for j in range(0, len(car_names[i])):
                self.driver.get(car_curris[i][j])
"""


if __name__ == "__main__":
    EspolCatalogSearch().test_exercise()