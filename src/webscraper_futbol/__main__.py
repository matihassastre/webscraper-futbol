import argparse
import csv
from .scrapers.fbref_scraper import get_table, extract_standings
from .config import standings_url

def main():
    parser = argparse.ArgumentParser(prog="webscraper-futbol")
    parser.add_argument("--season", type=int, default=2025)
    args = parser.parse_args()

    url = standings_url(args.season)
    soup = get_table(url)
    rows = extract_standings(soup)

    # guardamos CSV
    out = f"data/standings_{args.season}.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)

    print(f"✅ Filas: {len(rows)} guardado en {out}")
    print("🔹 Muestra:")
    for r in rows[:5]:
        print(r)

if __name__ == "__main__":
    main()
