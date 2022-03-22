import time
import datetime
from selenium import webdriver
import yaml
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

date_today  = datetime.datetime.now()
desire_date = date_today + datetime.timedelta(days=8)

with open('/Users/yudiyang/Desktop/autoRegister/autoRegister/login.yaml', 'r') as f:
  config = yaml.safe_load(f)

driver = webdriver.Chrome(ChromeDriverManager().install())

def login(username, password):
  driver.get('https://lt.clubautomation.com')
  driver.maximize_window()
  driver.find_element(By.ID, 'login').send_keys(username)
  driver.find_element(By.ID, 'password').send_keys(password)
  driver.find_element(By.ID, 'loginButton').click()
  time.sleep(3)
  driver.find_element(By.ID, 'menu_reserve_a_court').click()
  time.sleep(2)
  driver.find_element(By.ID, 'date').clear()
  driver.find_element(By.ID, 'date').send_keys(desire_date.strftime("%m/%d/%Y"))
  try:
    itv_btn = driver.find_element(By.XPATH, "//input[@type='radio' and @value='120']")
    itv_btn.find_element(By.XPATH, '..').click()
    driver.find_element(By.ID, 'reserve-court-search').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "8:00pm").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@id='confirm']").click()
    print('Reserved Court for Date:', desire_date.strftime("%m/%d/%Y"))
    time.sleep(5)
  except:
    print('No desire time avaiable.')
  driver.quit()
  


def main():
  login(config['email'], config['password'])

if __name__=='__main__':
  main()