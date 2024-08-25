from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def webdriver_wait(driver,elemtn_tuple):
    WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located(elemtn_tuple))