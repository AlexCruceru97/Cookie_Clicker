from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(20)
clicker = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
items = driver.find_elements(By.CSS_SELECTOR, '#store div')
i=0
while i<5000:
    clicker.click()
    cookies = driver.find_element(By.ID, 'cookies')
    cursor = driver.find_element(By.ID, 'productPrice0')
    grandma = driver.find_element(By.ID, 'productPrice1')
    product2 = driver.find_element(By.ID, 'productPrice2')
    product3 = driver.find_element(By.ID, 'productPrice3')
    # because cookies.text return a string "x cookies" we split with space and take first part and then convert to int
    cookies_nr = int(cookies.text.split()[0])

    if int(cookies_nr) > int(grandma.text):
        buy_product = driver.find_element(By.ID, 'product1')
        buy_product.click()
    elif int(cookies_nr) > int(cursor.text):
        buy_product = driver.find_element(By.ID, 'product0')
        buy_product.click()
    i += 1
