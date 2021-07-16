from selenium import webdriver
from datetime import datetime

def login():
    driver = webdriver.Firefox()
    driver.get("URL of your website")
    username = driver.find_element_by_id('user-id') # Replace user-id with the ID your website uses for username Textbox
    paswrd = driver.find_element_by_id('pw-id')  # Replace pw-id with the ID your website uses for password Textbox

    username.send_keys('saiharish@softcell.com')
    print('Username Entred successfully')

    paswrd.send_keys('saiharish@123')
    print('Password entred successfully')

    login_button = driver.find_element_by_xpath("//input[@type='submit' and @value='Sign In']").click() # replace Sign In to what your button value is
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

    
