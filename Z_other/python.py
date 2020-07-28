from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

a = driver.find_element_by_xpath('//*[@id="lg"]/map/area').is_displayed()
print(a)
time.sleep(10)
driver.quit()
