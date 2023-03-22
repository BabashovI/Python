from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.headless = True
browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
stealth(browser,
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
browser.get("https://frs.gov.cz/en/ioff/application-status")
time.sleep(2)
app_Number = "edit-ioff-application-number"
app_Code = "edit-ioff-application-code"
app_Year = "edit-ioff-application-year"
app_Submit = "Verify"  # "edit-submit-button"

Number = browser.find_element(By.ID, f"{app_Number}").send_keys("83495")
Code = browser.find_element(By.ID, f"{app_Code}").send_keys("ZM")
Year = browser.find_element(By.ID, f"{app_Year}").send_keys("2022")
SubMit = browser.find_element(
    By.XPATH, value="//button[@value='Verify']").click()
data = browser.find_element(By.CLASS_NAME, "col-sm-12")
placeHolder = data.find_element(By.CLASS_NAME, "placeholder").text
status = data.find_element(By.CLASS_NAME, "alert-warning").text

print(f"{placeHolder} :: {status}")

browser.close()
browser.quit()
