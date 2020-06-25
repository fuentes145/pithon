from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.wikipedia.org")
driver.implicitly_wait(10)
sercher = driver.find_element_by_xpath('//*[@id="searchInput"]')
sercher.send_keys('Michael Jordan')

serch_boton = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
serch_boton.click()@@d