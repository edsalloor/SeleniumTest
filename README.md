# SeleniumTest
Test exercise for ioet

### Python interpreter:
  3.7

### Required libraries:
* selenium
* webdriver_manager
* csv

**Runner:** exercise.py

### Description:
The file locators.py contains the xpath expressions that I used to find the elements in the ESPOL catalog page, the main xpath that I identified is in FACULTY_DIV that give me the div for each faculty, the others xpaths: FACULTY_DIV, FACULTY_LI, LINK, are relative to FACULTY_DIV.
In the main thread ChromeDriverManager installs a chrome driver if it does't find a path to a default binary, so it will be necesary to install the package webdriver_manager via:
```
    pip install webdriver_manager
```
The first exercise ends when the text "The file test_exercise.csv has been created" is printed in console, then you can open this file in the project directory to check all the careers offered in the ESPOL catalog with the following format:
```
    career_name_en,career_code,faculty_name,link_to_career_curriculum
```
    
### Bonus:
The bonus exercise runs immediately after the first exercise, it could take much longer since it will crawling all the curriculum pages of each career, but you can look the progress in console since there are being printed the elective courses gotten for each career.
In the bonus exercise goes over all the curriculum links obtained in the previous exercise and opens them in a chrome driver. For each curriculum page, first the "Elective course" ("a" element) is clicked to display the table of complementary subjects, then it waits for the number of table rows selector to be clickable, clicks the last option (all the rows) and waits for the table, finally the program scraps the table's rows to get the name and the code of each complementary subject.
The progrma ends when the text "The file bonus_exercise.csv has been created" is printed in console, then you can open this file in the project directory to check all the elective subjects for each career with the following format:
```
    elective_subject_code,elective_subject_name_en
```
The subjects in that file are sectioned by the career.
