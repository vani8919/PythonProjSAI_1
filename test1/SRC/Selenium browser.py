import time

from selenium import webdriver

# service obj =Services("path")
# driver = webdriver.chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/")

time.sleep(2)            