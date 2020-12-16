import sys

from pyscraper import pyscraper

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Missing URL parameter. Usage: pyscraper <url_to_scrape>")

    report = pyscraper.scrape_url(str(sys.argv[1]))

    # as stated in https://docs.python.org/3/howto/logging.html#when-to-use-logging, for this script's main purpose,
    # the right tool to use is just "print()". This is why I did not use logging.info(), etc...

    print(f"Number of HTML elements: {report['total']}")

    print("Most frequently used elements (Top 5):")

    [print(tag, ":", occurrences) for (tag, occurrences) in report['top5']]
