from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)
try:
    browser.get("https://www.lg.com/uk/monitors/all-monitors/?ec_model_status_code=ACTIVE")
    price_elements = browser.find_elements(By.CLASS_NAME, "c-price__purchase")
    print(f"Found {len(price_elements)} elements with class 'c-price__purchase'")
    # Extract and log prices
    with open("price_log.txt", "a") as f:
        f.write(f"\nScrape at {time.ctime()}:\n")
        for i, element in enumerate(price_elements, 1):
            price = element.text.strip()
            print(f"Price {i}: {price}")
            f.write(f"Price {i}: {price}\n")
finally:
    browser.quit()