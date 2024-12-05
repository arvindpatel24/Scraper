# Scraper

Simple scrapping tool for DentalStall using Beautiful soup, request and redis library.

### Python Virtual Environment Setup -

https://www.hostinger.in/tutorials/how-to-create-a-python-virtual-environment

## Steps -

1. Clone the repo
2. Make sure redis installed and running - https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/
3. Setup Virtual Environment for Python - https://www.hostinger.in/tutorials/how-to-create-a-python-virtual-environment

   a. `python3 -m venv env`

   b. `source env/bin/activate`

4. Install library from requirements.txt - `pip install -r requirements.txt`
5. Run the server - `python -m uvicorn main:app --reload`
6. Test the api through - http://localhost:8000/docs
