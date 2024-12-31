from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# Set up the Selenium WebDriver
driver = webdriver.Chrome() 
url = "https://x.com/Jaguar/status/1858800846646948155"
driver.get(url)

# Allow time for the page to load
time.sleep(5)

tweets_data = []  # List to store tweet text and dates
for _ in range(10):  # Adjust range for more scrolls
    tweet_elements = driver.find_elements(By.CSS_SELECTOR, "article")
    for element in tweet_elements:
        try:
            # Extract the tweet text
            tweet_text = element.find_element(By.CSS_SELECTOR, "div[lang]").text
            
            # Extract the date (time element contains the timestamp)
            timestamp_element = element.find_element(By.TAG_NAME, "time")
            tweet_date = timestamp_element.get_attribute("datetime")  # ISO 8601 format
            
            # Append tweet data
            tweets_data.append((tweet_text, tweet_date))
        except Exception as e:
            # Skip if any element is missing (e.g., ad tweets)
            continue
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(5)  # Allow time for loading more tweets

# Remove duplicates
tweets_data = list(set(tweets_data))

# Save tweets to a CSV file
with open("tweets_with_dates.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Tweet", "Date"])
    for tweet_text, tweet_date in tweets_data:
        writer.writerow([tweet_text, tweet_date])


driver.quit()
print("Scraping completed and saved to tweets.csv")
