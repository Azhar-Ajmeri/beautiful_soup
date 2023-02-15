# importing modules
import logging
from urllib.error import HTTPError, URLError

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')


def get_page_source(page_url: str):
    """
    This function fetches the page for provided URL.
    :param page_url: str.
    :return: str.
    """
    response = requests.get(page_url)
    response.raise_for_status()
    return response.content


def parser_for_information(page_source):
    """
    This function parses the page source using beautiful soup library and extracts information from soup's object.
    :param page_source: str.
    :return: None.
    """
    soup = BeautifulSoup(page_source, 'html.parser')
    # Attributes usage
    print(soup.title.string)
    print([tag.string for tag in soup.findAll("span", class_="text")])


def main(page_url):
    try:
        page_source = get_page_source(page_url)
        parser_for_information(page_source)
    except HTTPError as hp:
        logging.info(str(hp))
    except URLError as ue:
        logging.info(str(ue))
    except requests.exceptions.HTTPError as e:
        logging.info(str(e))
    except requests.exceptions.RequestException as e:
        logging.info(str(e))


if __name__ == '__main__':
    url = 'https://quotes.toscrape.com/'
    main(url)
