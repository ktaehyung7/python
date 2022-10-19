# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    driver = webdriver.Chrome("C:/Temp/chromedriver.exe")
    driver.get("http://www.naver.com")
    #driver.get("http://thk8.netlify.app")
    time.sleep(5)

    elem = driver.find_element(By.ID, "query")
    elem.clear()
    elem.send_keys("카카오 장애")
    elem.send_keys(Keys.RETURN)
    #elem.click()
    time.sleep(20)
    assert "No results found." not in driver.page_source

    driver.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
