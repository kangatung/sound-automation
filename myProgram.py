from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def youtube(judul):
    service = Service(executable_path='/path/to/chromedriver')
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 100)


    driver.get('https://www.youtube.com/')
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.ID,'search-input').click()
    search = wait.until(EC.element_to_be_clickable((By.NAME,'search_query')))
    search.send_keys(f'{judul}' + Keys.ENTER)

    driver.find_element(By.NAME,'search_query')
    clickVideo = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]/yt-formatted-string')))
    clickVideo.click()

    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='skip-button:6']/span/button")))
        element.send_keys(Keys.ENTER)
        time.sleep(360)
    except:
        pass
        time.sleep(360)

