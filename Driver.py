from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
input("Press Enter to close the browser...")
driver.quit()

