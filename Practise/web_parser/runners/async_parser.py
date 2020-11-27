import asyncio

from aiohttp import ClientSession

from Practise.web_parser.common import REQUEST_HEADERS, input_goods, make_async_request, time_it
from Practise.web_parser.config import PHARMACY_COOKIE
from Practise.web_parser.parser import parse_html


async def async_parser(goods):
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession(headers=REQUEST_HEADERS, cookies=PHARMACY_COOKIE) as session:
        for good in goods:
            task = asyncio.ensure_future(make_async_request(good, session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable

    results = []
    for resp in responses:
        if resp is None:
            continue
        results.extend(parse_html(resp))
    print(f'Done with {len(results)} results')


@time_it
def run():
    """Parse site asynchronously"""
    goods = input_goods()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(async_parser(goods))
    loop.run_until_complete(future)
