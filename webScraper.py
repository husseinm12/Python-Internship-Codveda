import requests
from bs4 import BeautifulSoup
import csv

url = "https://techcrunch.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
response = requests.get(url , headers=headers)
if response.status_code != 200:
    print("Failed to retrieve the pae")
    exit

# parse the HTML content using BeautifulSoup

soup = BeautifulSoup(response.content, 'html.parser')

# extract specific data (article title and URLs)

articles = soup.find_all('a', class_='loop-card__title-link')

scraped_data = []
for article in articles:
    title = article.get_text(strip=True)
    link = article['href']
    scraped_data.append({
        'Title': title,
        'URL' : link
  })
    
# save data into a csv file

with open("C:/Users/vtouch/Desktop/Level 2/Task 2/data.csv", 'w') as file:
    fieldnames = ['Title','URL']
    writer= csv.DictWriter(file,fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)   
    print(f" Scraped {len(scraped_data)} articles and saved to csv file") 


