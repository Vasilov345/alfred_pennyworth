from bs4 import BeautifulSoup

from Practise.web_parser.raw_html import html


def _normalize_title(title: str):
    return title


def _normalize_price(price: str):
    return price


def parse_html(html: str):
    """
    Args:
        html: - html text to parse
    Returns:

    """
    soup = BeautifulSoup(html, 'html.parser')
    html_results = soup.select('.results-wrapper')

    if html_results:
        html_results = html_results[0]
    else:
        print("Results not found")
        exit(0)

    # видаляю аналоги для препарату
    for analogue in html_results.select('tbody.analogue'):
        analogue.decompose()

    # TODO normalize price and title
    # - remove грн from price
    return tuple(
        (_normalize_title(title.text), _normalize_price(price.text)) for title, price in zip(
            html_results.select('td.col1 .item-title'),
            html_results.select('td.col4 .item-price')
        )
    )


if __name__ == '__main__':
    parse_html(html)
