from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel
from auth import authenticate
from scrape import Scrape
from store import Storage
from notification import Notification

app = FastAPI()

class ScrapeRequest(BaseModel):
    total_pages: int = 1
    proxy: str | None = None

@app.post("/scrape")
def scrape_data(request: ScrapeRequest, token: str = Depends(authenticate)):
    scraper = Scrape()
    store = Storage()
    notify = Notification()

    products = scraper.scrape_pages(request.total_pages, request.proxy)
    # products[0]['product_price'] = "₹1195.00"
    updated_products = store.save_products(products)
    notify.notify(len(products), updated_products)
    return {"status": "success", "total_product_scraped" : len(products), "updated_products_db": updated_products}

class ScrapeRequest(BaseModel):
    total_pages: int = 1
    proxy: str | None = None

@app.get("/get_product")
def get_product_from_cache(title: str = Query(title = "product_title", description="Product title is reuired in the query param."), token: str = Depends(authenticate)):
    store = Storage()
    product = store.fetch_cache(title)
    return product
