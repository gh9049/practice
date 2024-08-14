from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Connect to the remote WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the website (if not already on the page)
driver.get("https://flowgpt.com/flux")

# Wait for the "Claim" button to be clickable
claim_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Claim')]"))
)

# Click the "Claim" button
claim_button.click()

#Close the browser (optional)
driver.quit()
