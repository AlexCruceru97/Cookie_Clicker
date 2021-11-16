from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

#driver.get("https://www.amazon.com/Nike-Monarch-Trainer-Black-White-Racer-Regular/dp/B0059OZ0OI/ref=sr_1_3?crid=3M7L1NN3QAZNJ&dchild=1&keywords=nike&qid=1635879641&qsid=136-4024510-7777551&sprefix=ni%2Caps%2C317&sr=8-3&sres=B07NLVK1NP%2CB078NG6LRD%2CB07RGLZXKH%2CB07YKR5FR4%2CB083PV5VCH%2CB01CB0UPZ6%2CB07FKCK3KK%2CB07H8J1QV9%2CB0921WFDGW%2CB0798P35QF%2CB08RMZNYNB%2CB072QXS3JD%2CB004Y6PQBE%2CB00E4Z0034%2CB08NYFPGQ8%2CB07TKMNN8J%2CB07Y856JTW%2CB095XWY37G%2CB00K5CN73A%2CB007T2HB7C&th=1&psc=1")
driver.get("https://www.python.org/")
#logo = driver.find_element(By.CLASS_NAME, "python-logo")
#print(logo.size)
#documentation = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
#print(documentation.text)

bug_link=driver.find_element(By.XPATH, '/html/body/div/footer/div[2]/div/ul/li[3]/a')
print(bug_link.text)

#events_list = []

events = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')

# for event in events:
#     print(event.text)
#     events_list.append(event.text)


dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')

dict = {}
for n in range(len(dates)):
    dict[n]={
        "time": dates[n].text,
        #"name": events_list[n],
        "name": events[n].text,
    }
print(dict)
driver.quit()