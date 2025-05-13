
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime

import pandas as pd

# Use UTF-8 encoding when reading the file
df = pd.read_csv("/Users/ifureemmanueludo/web_scrapper_project/html_scraper/amazon_products.csv", encoding="utf-8")
print(df.head())

def main():
    # Amazon product URLs to scrape
    product_urls = [
        "https://www.amazon.com/Hisense-Premium-65-Inch-Compatibility-65U8G/dp/B091XWTGXL/?th=1",
        "https://www.amazon.com/dp/B08TKSMQSY/?th=1",
        "https://www.amazon.com/dp/B08WJMQ5TG/?th=1",
        "https://www.amazon.com/SAMSUNG-86-inch-Crystal-TU9010-Built/dp/B094C627M5/"
    ]

    # Set Chrome options with a user-agent
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Output file
    output_file_name = 'output-{}.csv'.format(datetime.today().strftime("%m-%d-%Y"))
    fieldnames = [
        "price", "title", "rating", "Brand Name", "Item Weight", "Product Dimensions", "Country of Origin",
        "Item model number", "Is Discontinued By Manufacturer", "Output Wattage", "Color Name",
        "Specification Met", "Special Features", "Speaker Type", "ASIN", "Customer Reviews",
        "Best Sellers Rank", "Date First Available"
    ]

    all_data = []

    for url in product_urls:
        print(f"\n🔗 Visiting: {url}")
        driver.get(url)
        time.sleep(5)  # Allow content to load

        # Scroll to bottom of the page to trigger dynamic content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "productTitle"))
            )
        except:
            print(f"⚠️ Page didn't load fully for: {url}")
            continue

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract title
        title = soup.find("span", {"id": "productTitle"})
        title = title.get_text(strip=True) if title else ""

        # Extract price
        price_elem = (
            soup.select_one("span.a-price span.a-offscreen")
            or soup.select_one("#price_inside_buybox")
            or soup.select_one("#priceblock_ourprice")
            or soup.select_one("#priceblock_dealprice")
        )
        price = price_elem.get_text(strip=True).replace("$", "").replace(",", "") if price_elem else ""

        # Extract rating
        rating_elem = (
            soup.select_one("i.a-icon-star span.a-icon-alt")
            or soup.select_one("span[data-asin-rating]")
        )
        rating = rating_elem.get_text(strip=True).split(" ")[0] if rating_elem else ""

        # Extract customer reviews
        review_elem = soup.select_one("#acrCustomerReviewText")
        review_count = review_elem.get_text(strip=True) if review_elem else ""

        # Extract best sellers rank
        rank_text = ""
        product_details_div = soup.find("div", id="detailBulletsWrapper_feature_div")
        if product_details_div:
            for li in product_details_div.select("li span.a-list-item"):
                if "Best Sellers Rank" in li.text:
                    rank_text = li.get_text(strip=True).replace("\u200e", "")
                    break

        # Tech specs table
        tech_specs = {}
        table_sections = soup.find_all("table", {"class": "prodDetTable"})
        for table in table_sections:
            for row in table.find_all("tr"):
                header = row.find("th")
                value = row.find("td")
                if header and value:
                    key = header.get_text(strip=True)
                    val = value.get_text(strip=True)
                    tech_specs[key] = val

        data = {
            "price": price,
            "title": title,
            "rating": rating,
            "Brand Name": tech_specs.get("Brand", ""),
            "Item Weight": tech_specs.get("Item Weight", ""),
            "Product Dimensions": tech_specs.get("Product Dimensions", ""),
            "Country of Origin": tech_specs.get("Country of Origin", ""),
            "Item model number": tech_specs.get("Item model number", ""),
            "Is Discontinued By Manufacturer": tech_specs.get("Is Discontinued By Manufacturer", ""),
            "Output Wattage": tech_specs.get("Output Wattage", ""),
            "Color Name": tech_specs.get("Color Name", ""),
            "Specification Met": tech_specs.get("Specification Met", ""),
            "Special Features": tech_specs.get("Special Features", ""),
            "Speaker Type": tech_specs.get("Speaker Type", ""),
            "ASIN": soup.select_one("#ASIN")["value"] if soup.select_one("#ASIN") else "",
            "Customer Reviews": review_count,
            "Best Sellers Rank": rank_text,
            "Date First Available": tech_specs.get("Date First Available", "")
        }

        all_data.append(data)

    # Write to CSV
    with open(output_file_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)

    print(f"\n✅ Scraping complete. Data saved to {output_file_name}")
    driver.quit()


if __name__ == "__main__":
    main()
