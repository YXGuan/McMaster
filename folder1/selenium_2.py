from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/home/yuxiang/node_modules/chromedriver/lib/chromedriver/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://google.com")
print(driver.title)

search = driver.find_element_by_class_name("s")

search.send_keys("test")

search.send_keys(Keys.RETURN)


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")

    for article in articles:
        header = article.find_element_by_class_name("entry-summery")
        print(header.text)
finnaly:
    driver.quit()