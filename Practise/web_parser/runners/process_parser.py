import multiprocessing as mp
from Practise.web_parser.common import input_goods, make_sync_request, time_it
from Practise.web_parser.parser import parse_html


@time_it
def run():
    """Parser by processes"""
    pool = mp.Pool(mp.cpu_count())
    goods = input_goods()
    results = []

    async_results = [
        pool.apply_async(make_sync_request, args=(good,))
        for good in goods
    ]  # is a list of pool.ApplyResult objects

    for resp in (res.get() for res in async_results):
        if resp is None:
            continue
        results.extend(parse_html(resp.text))
    print(f'Done with {len(results)} results')
