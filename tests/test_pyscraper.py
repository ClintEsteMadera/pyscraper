#!/usr/bin/env python

"""Tests for `pyscraper` package."""
import os
from urllib.error import HTTPError

import pytest

from pyscraper import pyscraper

positiveScenarios = [
    # we don't fail on invalid HTML as we don't actually check input validity (we only check non-emptiness)
    ('invalid.html', 0, []),
    ('only_doctype_declaration.html', 0, []),
    ('valid_no_closing_tags.html', 3, [('html', 1), ('head', 1), ('body', 1)]),
    ('valid_with_only_four_tags.html', 4, [('html', 1), ('head', 1), ('body', 1), ('div', 1)]),
    ('valid.html', 276, [('a', 56), ('div', 50), ('li', 23), ('meta', 20), ('p', 18)]),
    ('valid2.html', 1105, [('div', 452), ('script', 164), ('span', 88), ('a', 70), ('li', 60)]),
]


@pytest.mark.parametrize("input_file,expected_total,expected_top5", positiveScenarios)
def test_scraping_valid_inputs(input_file, expected_total, expected_top5):
    """
    pyscraper.scrape(htmlContent) Test scenarios that should return a concrete value
    """
    report = pyscraper.scrape(_read_test_data_file(input_file))

    assert report['total'] == expected_total
    assert report['top5'] == expected_top5


@pytest.mark.parametrize("content", [None, ''])
def test_scraping_empty_content(content):
    """
    pyscraper.scrape(url) Test scenarios that end up in an error being raised due to empty input
    """
    with pytest.raises(ValueError):
        pyscraper.scrape(content)


@pytest.mark.parametrize("url,expected_exception_type", [
    (None, ValueError),
    ('not_a_valid_uri', ValueError),
    ('http://non-existent-domain.com/bla', HTTPError),
])
def test_scraping_bad_urls(url, expected_exception_type):
    """
    (Integration Test, as it uses HTTP requests)
    pyscraper.scrape_url(url) Test scenarios that end up in an error being raised due to malformed or invalid URLs
    """
    with pytest.raises(expected_exception_type):
        pyscraper.scrape_url(url)


def test_scraping_valid_url_that_returns_non_html_data():
    """
    (Integration Test, as it issues a HTTP request)
    pyscraper.scrape_url(url) Make sure that hitting a valid URI that returns non-HTML data works as expected
    """
    report = pyscraper.scrape_url('https://scotthelme.co.uk/.well-known/security.txt')

    assert report['total'] == 0
    assert report['top5'] == []


def _read_test_data_file(file_name):
    return open(f"{os.path.dirname(__file__)}/data/{file_name}", 'r').read()
