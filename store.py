from fastapi import HTTPException
from env import FILENAME
import json
import redis

class Storage:
    def save_products(self, products):
        updated_count = 0
        for product in products:
            r = redis.Redis(decode_responses=True)
            cache_product = r.get(product['product_title'])
            if cache_product:
                json_value = json.loads(cache_product)
                if(json_value['product_price'] != product['product_price']) :
                    updated_count += 1
                    r.set(product['product_title'], json.dumps(product))
            else:
                updated_count += 1
                r.set(product['product_title'], json.dumps(product))

        json_object = json.dumps(products, indent=4, ensure_ascii=False)
        with open(FILENAME, "w") as outfile:
            outfile.write(json_object)

        return updated_count
    
    def fetch_cache(self,product_title):
        r = redis.Redis(decode_responses=True)
        cache_product = r.get(product_title)
        if cache_product:
            json_value = json.loads(cache_product)
            return json_value
        else:
            raise HTTPException(status_code=404, detail="Not Found")
