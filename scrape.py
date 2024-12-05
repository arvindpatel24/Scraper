import requests
from bs4 import BeautifulSoup
import time
# import json

class Scrape:
    def __init__(self, proxy=None):
        self.base_url = "https://dentalstall.com/shop/"
        self.retries = 3
        self.delay = 5
    
    def scrape_pages(self, total_pages=1, proxy = None):
        products = []
        for page in range(total_pages):
            for _ in range(self.retries):
                try:
                    url = self.base_url + 'page/' + str(page+1)
                    print(url)
                    response = requests.get(url, proxies={"http": proxy, "https": proxy} if proxy else None)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        cards = soup.find_all("div", class_ = "product-inner")
                        for card in cards:
                            product_title = card.find('h2').text
                            product_price = card.find('span', class_="price").find('bdi').text
                            product_price = f'{product_price}'
                            path_to_image = card.find('noscript').find("img")["src"]
                            products.append({"product_title": product_title, "product_price": product_price, "path_to_image": path_to_image})
                        break
                except Exception as err:
                    print("Error-", err)
                    time.sleep(self.delay)
                    continue
        return products


# scraper = Scrape()
# products = scraper.scrape_pages(2)

# products = [{'product_title': '1 x GDC Extraction Forceps Lo...', 'product_price': '₹850.00₹1250.00', 'path_to_image': 'https://dentalstall.com/wp-content/uploads/2021/11/GDC-Extraction-Forceps-Lower-Molars-86A-Standard-FX86AS-300x300.jpg'}]

# json_object = json.dumps(products, indent=4, ensure_ascii=False)
 
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)