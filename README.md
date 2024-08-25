- Name : Veeresh
- Author : Veeresh

## Web Automation Framework with POM in Python(Selenium)
- Python, PyTest
- Selenium
- Allure Report
- Gitignore, PyTest Report
- Page Object Model and Page Factory both
- Highlight element while run
- Parallel Run with xdist
- MY SQL data base connect to verify data.

### Folder Structure

<img width="944" alt="Screenshot" src=""

### All the dependencies used
````
- pip install allure-pytest selenium
- pip install pytest selenium pytest-html openpyxl 
- pip install selenium-page-factory 
- pip install pyyaml faker openpyxl
- pip install pytest-xdist 
- pip install mysql-connector-python
- pip install pytest-reportportal 
````


### Install all in the one Go

````
pip install allure-pytest selenium pytest openpyxl faker pytest-xdist pytest-html
````

### How to run the Framework?
````
pytest -n auto tests/vwoLoginTests/pom/test_*
````

