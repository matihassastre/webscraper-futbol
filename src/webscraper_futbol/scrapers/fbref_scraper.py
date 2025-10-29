import requests
from bs4 import BeautifulSoup

def get_table(url: str):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html5lib")

def extract_standings(soup: BeautifulSoup):
    table = soup.find("table")
    if not table:
        return []
    rows = []
    for tr in table.select("tbody tr"):
        cells = [c.get_text(strip=True) for c in tr.find_all(["th", "td"])]
        if cells:
            rows.append(cells)
    return rows
