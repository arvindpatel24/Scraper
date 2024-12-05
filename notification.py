class Notification:
    def notify(self, products_scraped, product_updated_db):
        print(f"Scraping completed. Total {products_scraped} products scraped and {product_updated_db} products updated the DB.")