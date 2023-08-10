from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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
    if driver.find_element(By.XPATH, '/html/body/app-root/app-after-login/div/mat-sidenav-container/mat-sidenav-content/div/app-student-home-tabs/div[1]/app-student-to-do/mat-card/app-to-do-list/div[1]/div/h3'):
        print("No tasks due!")
    else:
        # TODO Make summary
        pass

