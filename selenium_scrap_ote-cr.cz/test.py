from typing import Any
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://ote-cr.cz/en")
assert "Welcome" in driver.title
elem = driver.find_element(By.CLASS_NAME, "wrap")
h3 = driver.find_element(By.TAG_NAME, "href")
print(h3.text)
# elem.clear()
# elem.send_keys("GAS")
# elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()
