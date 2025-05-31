import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

URL = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:    
    # Get the page
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    print(f"Página obtenida correctamente")
except requests.exceptions.RequestException as e:
    print(f"Error al obtener la página: {e}")
    exit(1)

# Parse the page
try:
    soup = BeautifulSoup(response.text, "html.parser")
    print(f"Página analizada correctamente")
except Exception as e:
    print(f"Error al analizar la página: {e}")
    exit(1)

# Find all product cards
try:
    product_cards = soup.find_all("article", class_="product_pod")
    print(f"Productos encontrados correctamente")
except Exception as e:
    print(f"Error al encontrar los productos: {e}")
    exit(1)

# Initialize lists to store data
product_names = []
product_prices = []
product_links = []

# Extract product information
try:
    for card in product_cards:
        name = card.find("h3").find("a").text.strip()
        price = card.find("p", class_="price_color").text.strip().replace("Â£", "£")
        link = card.find("h3").find("a")["href"]

        product_names.append(name)
        product_prices.append(price)
        product_links.append(link)

    print(f"Productos extraídos correctamente")
    print(f"Nombres: {len(product_names)}")
    print(f"Precios: {len(product_prices)}")
    print(f"Enlaces: {len(product_links)}")
except Exception as e:
    print(f"Error al extraer los productos: {e}")
    exit(1)

#Guardamos el documento en un csv
df = pd.DataFrame({
    "product_names": product_names,
    "product_prices": product_prices,
    "product_links": product_links
})

df.to_csv("data/books.csv", index=False, encoding='utf-8-sig')

print(f"Datos guardados en books.csv")



