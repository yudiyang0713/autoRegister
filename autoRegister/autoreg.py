import time
import datetime
from selenium import webdriver
import yaml
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def login(username, password):
  driver.get(r'https://lt.clubautomation.com')
  driver.maximize_window()
  driver.find_element(By.ID, 'login').send_keys(username)
  driver.find_element(By.ID, 'password').send_keys(password)
  driver.find_element(By.ID, 'loginButton').click()
  time.sleep(3)
  driver.find_element(By.ID, 'menu_reserve_a_court').click()
  time.sleep(2)
  driver.find_element(By.ID, 'date').clear()
  driver.find_element(By.ID, 'date').send_keys(desire_date.strftime("%m/%d/%Y"))
  if(desire_date.weekday() == 0 or desire_date.weekday() == 2):
    if(not register("120", "8:00pm"))：
      register("60", "8:30pm")
  elif(desire_date.weekday() == 1 or desire_date.weekday() == 3):
    register("60", "8:30pm")

def register(period, start_time):
  try:
    itv_btn = driver.find_element(By.XPATH, "//input[@type='radio' and @value='"+period+"']")
    itv_btn.find_element(By.XPATH, '..').click()
    driver.find_element(By.ID, 'reserve-court-search').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, start_time).click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@id='confirm']").click()
    print('Reserved Court for Date:', desire_date.strftime("%m/%d/%Y"))
    time.sleep(5)
    log = "Reserved Court for Date:"+desire_date.strftime("%m/%d/%Y")+"for "+start_time+"\n"
    with open(r'C:\Users\Yudi\Documents\GitHub\autoRegister\autoRegister\regist.log','a') as f:
        f.write(log)
        f.close()
    return True
  except:
    print('No desire time avaiable.')
    log = "No desire time avaiable."+desire_date.strftime("%m/%d/%Y")+"for "+start_time+"\n"
    with open(r'C:\Users\Yudi\Documents\GitHub\autoRegister\autoRegister\regist.log','a') as f:
        f.write(log)
        f.close()
    return False



def main():
  date_today  = datetime.datetime.now()
  desire_date = date_today + datetime.timedelta(days=8)

  with open(r'C:\Users\Yudi\Documents\GitHub\autoRegister\autoRegister\login.yaml','r') as f:
    config = yaml.safe_load(f)
    f.close()

  driver = webdriver.Chrome(ChromeDriverManager().install())
  login(config['email'], config['password'])
  driver.quit()

if __name__=='__main__':
  main()
