import requests
from bs4 import BeautifulSoup

def get_table(url: str):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html5lib")  # parser liviano
