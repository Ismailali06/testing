from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://google.com/')
driver.quit()
print ("sucess")

