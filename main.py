import sys

from pyscraper import pyscraper

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Missing URL parameter. Usage: pyscraper <url_to_scrape>")

    pyscraper.scrape_url(str(sys.argv[1]))
