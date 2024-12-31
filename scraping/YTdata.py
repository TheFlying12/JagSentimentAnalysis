import googleapiclient.discovery
import googleapiclient.errors
import csv
from google.colab import files
import os
from dotenv import load_dotenv

load_dotenv()
dev_key = os.getenv("YOUTUBE_DEV_KEY")

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = dev_key
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY
)

request = youtube.commentThreads().list(
    part="snippet",
    videoId="rLtFIrqhfng",
    maxResults = 30000
)
response = request.execute()

# Save the comments to a CSV file in the Colab filesystem
output_file = '/content/comments.csv'

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Comment'])  # Header row

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        writer.writerow([comment])  # Write each comment

print(f"Comments have been saved to {output_file}")

# Download the file to your local machine
files.download(output_file)
 