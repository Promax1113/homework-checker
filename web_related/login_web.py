from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from data_processing import make_summary


class HomeworkItem:
    def __init__(self, hw_data:dict):
        self.__name = hw_data['name']
        self.__course = hw_data['course']
        self.__due_date = hw_data['due_date']
        self.__homework_type = hw_data['type']
        self.__link = hw_data['link']

    def get_all(self):
        return {"name": self.__name, "course": self.__course, "due_date": self.__due_date, "type": self.__homework_type}



def login_to_web(url, username, password):
    print("Logging into the website...")
    chrome = Options()

    chrome.add_argument("--headless")
    chrome.add_argument("--disable-gpu")
    chrome.add_experimental_option('excludeSwitches', ['enable-logging'])

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
        page = BeautifulSoup(driver.find_element(By.XPATH, '/html/body/app-root/app-after-login/div/mat-sidenav-container/mat-sidenav-content/div/app-student-home-tabs/div[1]/app-student-to-do/mat-card/app-to-do-list/div[1]/div/mat-nav-list').get_attribute('innerHTML'), "html.parser") 
        homework_list = []
        for a_element in page.find_all("a", { "class":"mat-mdc-list-item mdc-list-item to-do-item mat-mdc-list-item-interactive mdc-list-item--with-leading-icon mdc-list-item--with-three-lines ng-star-inserted"}):
            link = a_element.get('href')
            span_element = a_element.find('span', class_='mdc-list-item__content')
            if span_element:
                homework_list.append({'name': span_element.find('h3').get_text(strip = True), 'course': span_element.find('p', class_='mat-mdc-list-item-line mdc-list-item__secondary-text app-foreground-secondary-text secondary to-do-course-title').get_text(strip = True), 'due_date': span_element.find('p', class_='mat-mdc-list-item-line mdc-list-item__secondary-text app-foreground-secondary-text secondary to-do-date').get_text(strip = True).strip('Due: '),'type':'assignment', 'link':link})
        homework_list_objs: list = []
        for hw in homework_list:
            item = HomeworkItem(hw)
            homework_list_objs.append(item)
    

    make_summary(homework_list_objs)

    
    
