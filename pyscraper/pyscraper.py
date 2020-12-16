#!/usr/bin/python3.9

"""Main module."""

import html.parser
import traceback
import urllib.request


class HtmlElementsCounter(html.parser.HTMLParser):
    """
    Specialized subclass of HTMLParser, which keeps track of HTML elements found in the input.
    The reason I went with this approach, is because HTML pages have a lot of gotchas to consider (e.g. DOCTYPE
    declarations, tags that are opened but not closed, etc.) and parsing the input manually (for example, using a Regex)
    would have been re-inventing the wheel. I assumed that for HTMLParser to be part of the standard libraries in Python,
    it must have been proven enough, both functionally speaking but also performance-wise. Internally, it does, though,
    perform more operations than strictly needed for this challenge but I decided to give it a go anyway as that overhead
    is negligible, considering the size of the problem we are solving. If this "scraper" would be used in the context,
    for instance, of a web spider or with a high volume of data, I would seriously reconsider this choice.
    """

    def __init__(self):
        super().__init__()
        self.occurrences_by_tag = {}

    def handle_starttag(self, tag, attrs):
        self.occurrences_by_tag[tag] = 1 + self.occurrences_by_tag.get(tag, 0)


def scrape_url(url):
    """
    Main function that performs a request to the provided URL and counts the HTML elements within, producing a report
    in the form of a Dictionary
    :param url: the URL of the webpage to fetch
    :return: see self.scrape(html_content)
    """
    # Some web servers reject requests without a User-Agent.
    # So, set a generic one, then, to avoid 403 (Forbidden) responses
    headers = {'User-Agent': "Mozilla/5.0"}
    try:
        response = urllib.request.urlopen(urllib.request.Request(url, headers=headers))
        # for the purpose of this code challenge, assuming UTF-8 should be good enough, in real life, we should be more
        # careful as some HTML content might use a different encoding.
        return scrape(response.read().decode("utf8"))
    except Exception:
        print(f"Error while scraping {url}. Details: {traceback.format_exc()}")
        raise


def scrape(html_content):
    """
    This function could have been a "private" utility but I left it "public" (note the quotation marks, as in Python
    there is no such thing as public or private access identifiers) because this scraping functionality could certainly
    be invoked passing raw HTML content, effectively circumventing the actual HTTP request. This has been useful, for
    instance, for unit testing this behavior.
    :param html_content: a string containing the actual HTML content. Cannot be None or empty.
    :return: a dictionary with two keys: "total" and "top5", containing the total number of elements and the count of
    the top 5 ones, respectively.
    """
    if not html_content:
        raise ValueError('Input is empty')

    parser = HtmlElementsCounter()
    parser.feed(html_content)
    parser.close()  # instructs the parser to consume the input entirely

    total = sum(parser.occurrences_by_tag.values())

    # if the input only has N different elements (N < 5), this dictionary will hold exactly N entries
    top5_elements_with_occurrences = sorted(parser.occurrences_by_tag.items(), reverse=True, key=lambda x: x[1])[:5]

    return dict(total=total, top5=top5_elements_with_occurrences)
