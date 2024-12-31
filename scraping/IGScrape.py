from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
from dotenv import load_dotenv


load_dotenv()
us = os.getenv("IG_username")
pwd = os.getenv("IG_password")

#print(us)

# # Set up the WebDriver
driver = webdriver.Chrome()

# # Navigate to Instagram and log in
driver.get("https://www.instagram.com")
time.sleep(5)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys(us)
password.send_keys(pwd)
password.send_keys(Keys.RETURN)
time.sleep(5)

# Navigate to the specific post
post_url = "https://www.instagram.com/p/DCjBohfvdj2/"
driver.get(post_url)
time.sleep(5)

############ SCRAPING BELOW #################

# Wait for the comments to load
# try:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul._a9ym"))
#     )
# except Exception as e:
#     print("Comments not found:", e)
#     driver.quit()
#     exit()

# Scroll to load all comments
comments = set()  # Use a set to avoid duplicates
while True:
    # Find all comment elements
    comment_elements = driver.find_elements(By.CSS_SELECTOR, "ul._a9ym")
    
    # Extract text from each comment
    for comment_element in comment_elements:
        try:
            # Extract the actual comment text
            comment_text = comment_element.find_element(By.CSS_SELECTOR, "span._ap3a._aaco._aacu._aacx._aad7._aade").text
            comments.add(comment_text)
        except Exception:
            continue

    # Scroll the comments container
    driver.execute_script("window.scrollBy(0, 300);")  # Scroll the window to load more comments
    time.sleep(2)  # Allow time for more comments to load

    # Check if new comments are loaded
    try:
        new_comment_elements = driver.find_elements(By.CSS_SELECTOR, "ul._a9ym")
        if len(new_comment_elements) == len(comment_elements):
            break  # No new comments loaded, stop scrolling
    except Exception:
        break


########### SCRAPING ABOVE #############


# Save to CSV
with open("instagram_comments.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Comment"])
    for comment in comments:
        writer.writerow([comment])

driver.quit()
print("Scraping completed and saved to instagram_comments.csv")
