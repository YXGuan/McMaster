from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://maccheck.mcmaster.ca/")

time.sleep(5)

email =  driver.find_element_by_id("i0116")
email.send_keys("guany27@mcmaster.ca") #Your email goes here 

next_b1 = driver.find_element_by_id("idSIButton9")
next_b1.click()

time.sleep(3)

password =  driver.find_element_by_id("i0118")
password.send_keys("Xme79453231.") #Your password goes here

next_b2 = driver.find_element_by_id("idSIButton9")
next_b2.click()

heck_yes = driver.find_element_by_id("idSIButton9")
heck_yes.click()

time.sleep(10)

option = driver.find_element_by_xpath('//*[@id="publishedCanvas"]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[4]/div/div/div/div/button')
option.click()