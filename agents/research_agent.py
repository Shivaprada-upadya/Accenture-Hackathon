import requests
from bs4 import BeautifulSoup

def scrape_trending_products():
    url = "https://example-ecommerce-site.com/trending"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = [tag.text for tag in soup.find_all('h2', class_='product-title')]
    return products