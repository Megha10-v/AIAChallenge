import requests
from bs4 import BeautifulSoup
from database import init_db, store_data

URL = "https://www.artificialintelligence-news.com/"

def scrape_ai_data():
    response = requests.get(URL)
    
    if response.status_code != 200:
        print("Failed to retrieve webpage")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    
    paragraphs = soup.find_all(['p','div']) 

    if not paragraphs:
        print("No text data found.")
        return []

    data = set()
    for para in paragraphs:
        text = para.get_text(strip=True)
        if text:  
            data.add((text,)) 
    return data


print("Initializing database...")
init_db()
    
print("Scraping AI news...")
scraped_data = scrape_ai_data()
    
if scraped_data:
    print(f"Storing {len(scraped_data)} data entries into database...")
    store_data(scraped_data)
else:
    print("No new data scraped.")
