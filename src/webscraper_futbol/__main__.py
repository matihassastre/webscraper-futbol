import argparse
from .scrapers.fbref_scraper import get_table

def main():
    parser = argparse.ArgumentParser(
        prog="webscraper-futbol",
        description="Scraper mínimo para probar el pipeline (requests + bs4 + html5lib)."
    )
    parser.add_argument("--url", default="https://example.com/",
                        help="URL a scrapear (default: https://example.com/)")
    args = parser.parse_args()

    soup = get_table(args.url)
    title = soup.title.text.strip() if soup.title else "(sin título)"
    print(f"Título: {title}")

if __name__ == "__main__":
    main()
