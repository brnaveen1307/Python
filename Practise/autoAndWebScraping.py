from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

# Start Selenium WebDriver (headless for automation)
service = Service('chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

# Product URL (example: Amazon laptop)
url = "https://www.amazon.in/s?k=laptop"
driver.get(url)

# Wait for JavaScript to load
time.sleep(3)

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract product data
products = []
for item in soup.select('.s-main-slot .s-result-item'):
    title = item.select_one('h2')
    price = item.select_one('.a-price-whole')
    rating = item.select_one('.a-icon-alt')

    if title and price:
        products.append({
            "Product Name": title.text.strip(),
            "Price (₹)": price.text.strip(),
            "Rating": rating.text.strip() if rating else "N/A"
        })

# Save to CSV
df = pd.DataFrame(products)
df.to_csv("amazon_laptop_prices.csv", index=False)

print("✅ Price data extracted successfully!")
driver.quit()
