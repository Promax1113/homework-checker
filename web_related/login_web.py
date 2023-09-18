from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from data_processing import make_summary


class HomeworkItem:
    def __init__(self):
        self.__name = "Sample"
        self.__course = "Sample Course"
        self.__due_date = "Sample Date"
        self.__homework_type = "Sample Work"
        self.__link = "http://localhost:8000"

    def get_all(self):
        return {"name": self.__name, "course": self.__course, "due_date": self.__due_date, "type": self.__homework_type, "link": self.__link}

    def set_all(self, _name, _course, _due_date, _type, _link):
        self.__name = _name
        self.__course = _course
        self.__due_date = _due_date
        self.__homework_type = _type
        self.__link = _link


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
    try: 
        tasks = driver.find_element(By.XPATH, '/html/body/app-root/app-after-login/div/mat-sidenav-container/mat-sidenav-content/div/app-student-home-tabs/div[1]/app-student-to-do/mat-card/app-to-do-list/div[1]/div/h3').text
        print("No tasks due!")
    except:
        print("You got homework...")
        print("Making summary...")
        print(driver.page_source)
        page = BeautifulSoup(driver.page_source, "html.parser") 
        print(page)  
        print(page.prettify())     
        elements = ["baller"]
        homework = []
        # TODO This is placeholder, I can't access my homework yet.
        for _item in elements:
            _item = HomeworkItem()
            _item.set_all("s", "s", "1969", "baller", "1234")
            homework.append(_item)
    # Pretend im getting elements from a list bruh
    #  * Gets elements *
    

    make_summary(homework)

    
    
