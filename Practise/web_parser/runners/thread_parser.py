import concurrent
from concurrent.futures.thread import ThreadPoolExecutor

from Practise.web_parser.common import input_goods, make_sync_request, time_it
from Practise.web_parser.parser import parse_html


@time_it
def run():
    """Parser by threads"""
    goods = input_goods()
    results = []

    with ThreadPoolExecutor() as executor:
        future_to_good = {executor.submit(make_sync_request, good): good for good in goods}
        # task = (executor.submit(make_sync_request, good) for good in goods)

        for future in concurrent.futures.as_completed(future_to_good):
            good = future_to_good[future]
            try:
                resp = future.result()
                if resp is None:
                    print(f'No results found for {good}')
                    continue
                results.extend(parse_html(resp.text))
            except Exception as exc:
                print('%r generated an exception: %s' % (good, exc))

    print(f'Done with {len(results)} results')

