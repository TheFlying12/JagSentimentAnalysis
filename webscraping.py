from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Replace with executable_path="path/to/chromedriver" if needed
url = "https://twitter.com/search?q=%23YourHashtag&src=typed_query&f=live"
driver.get(url)

# Allow time for the page to load
time.sleep(5)

# Scroll and extract tweets
tweets = []
for _ in range(10):  # Adjust range for more scrolls
    tweet_elements = driver.find_elements(By.CSS_SELECTOR, "article div[lang]")
    for element in tweet_elements:
        tweets.append(element.text)
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)  # Allow time for loading more tweets

# Remove duplicates
tweets = list(set(tweets))

# Save tweets to a CSV file
with open("tweets.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Tweet"])
    for tweet in tweets:
        writer.writerow([tweet])

driver.quit()
print("Scraping completed and saved to tweets.csv")
