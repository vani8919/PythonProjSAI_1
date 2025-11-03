import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.fed_cm import click_dialog_button

# service obj =Services("path")
# driver = webdriver.chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# XPATH //tagname[@attribute='value']
# CSS  tagname[attribute ='value']

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("sarvani")
driver.find_element(By.NAME,"email").send_keys("test@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("testone")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
messaage = driver.find_element(By.CLASS_NAME,"alert-success").text
print(messaage)
assert "Success" in messaage
time.sleep(2)














