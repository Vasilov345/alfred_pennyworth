import functools
import time

import requests
from aiohttp import ClientSession
from requests import Response

from Practise.web_parser.config import PHARMACY_COOKIE, SITE_URL

REQUEST_HEADERS = {
    'Accept': 'text/html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Accept-Language': 'en-us'
}


def input_goods():
    with open('./data/input_data_short.csv') as f:
        for line in f:
            yield line


def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print('%r  %2.2f ms' % (func.__doc__, (te - ts) * 1000))
        return result

    return wrapper


def make_sync_request(search_query: str) -> Response or None:
    try:
        resp = requests.get(url=f'{SITE_URL}/search?query={search_query}', cookies=PHARMACY_COOKIE,
                            headers=REQUEST_HEADERS)
        if resp.status_code != 200:
            print(f'Response status: {resp.status_code}. For {search_query}.')
            return None
        return resp
    except Exception as error:
        print(f'Error: {error}. For {search_query}.')
        return None


async def make_async_request(search_query: str, session: ClientSession) -> str or None:
    try:
        url = f'{SITE_URL}/search?query={search_query}'

        async with session.get(url) as response:
            resp = await response.read()

        if response.status != 200:
            print(f'Response status: {response.status}. For {search_query}.')
            return None
        return resp.decode(response.charset)
    except Exception as error:
        print(f'Error: {error}. For {search_query}.')
        return None