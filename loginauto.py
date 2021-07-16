from selenium import webdriver
from datetime import datetime

def login():
    driver = webdriver.Firefox()
    driver.get("http://mum9.softcell.com/")
    username = driver.find_element_by_id('user-id')
    paswrd = driver.find_element_by_id('pw-id')

    username.send_keys('saiharish@softcell.com')
    print('Username Entred successfully')

    paswrd.send_keys('saiharish@123')
    print('Password entred successfully')

    login_button = driver.find_element_by_xpath("//input[@type='submit' and @value='Sign In']").click()
    print('Login Successful')

def get_time():
    current_time = datetime.now().hour
    return current_time

    return current_time
if __name__ == '__main__':
    current_time = get_time()
    print(current_time)
    if current_time < 18:
        login()

    
