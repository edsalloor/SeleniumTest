# SeleniumTest
Test exercise for ioet

#### Runner: exercise.py

### Description:
The file locators.py contains the xpath expressions that I used to find the elements in the ESPOL catalog page, the main xpath that I identify is in FACULTY_DIV that give me the div for each faculty, the others xpaths: FACULTY_DIV, FACULTY_LI, LINK, are relative to FACULTY_DIV.
In the main thread ChromeDriverManager installs a chrome driver if it does't find a path to a default binary, so it will be necesary to install the package webdriver_manager via:
    pip install webdriver_manager
    
### Required libraries:
- selenium
- webdriver_manager
- csv
- page

### Python interpreter:
  3.7
