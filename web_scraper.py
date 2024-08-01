# web_scraper.py

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    print(f"Title of the webpage: {title}")

if __name__ == "__main__":
    main()
