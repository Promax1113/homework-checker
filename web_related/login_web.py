from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from data_processing import make_summary


class HomeworkItem:
    def __init__(self):
        self.name = "Sample"
        self.course = "Sample Course"
        self.due_date = "Sample Date"
        self.homework_type = "Sample Work"
        self.link = 

    def get_all(self):
        return {"name": self.name, "course": self.course, "due_date": self.due_date, "type": self.homework_type}

    def set_all(self, _name, _course,_due_date, _type):
        self.name = _name
        self.course = _course
        self.due_date = _due_date
        self.homework_type = _type


def login_to_web(url, username, password):
    print("Logging into the website...")
    chrome = Options()

    chrome.add_argument("--headless")
    chrome.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome)

    driver.get(url)
    driver.implicitly_wait(7)
    driver.find_element(By.XPATH, '/html/body/app-root/app-before-login/app-login/mat-toolbar/button[1]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/main/div/div/div/form/div[2]/div[1]/input').send_keys(username)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/main/div/div/div/form/div[2]/div[2]/input').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/main/div/div/div/form/div[2]/div[4]/span').click()
    driver.implicitly_wait(12)
    driver.find_element(By.XPATH, '/html/body/app-root/app-after-login/div/mat-sidenav-container/mat-sidenav-content/div/app-student-home-tabs/mat-tab-group/mat-tab-header/div/div/div/div[2]').click()
    make_summary()
    # if driver.find_element(By.XPATH, '/html/body/app-root/app-after-login/div/mat-sidenav-container/mat-sidenav-content/div/app-student-home-tabs/div[1]/app-student-to-do/mat-card/app-to-do-list/div[1]/div/h3'):
    #     print("No tasks due!")
    # else:
    #     pass

