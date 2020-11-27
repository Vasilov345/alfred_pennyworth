from Practise.web_parser.runners import async_parser, process_parser, sync_parser, thread_parser

if __name__ == '__main__':
    sync_parser.run()
    # Done with 20 results 'Sync parser' 19374.08 ms
    thread_parser.run()
    # Done with 20 results 'Parser by threads' 2632.93 ms
    process_parser.run()
    # Done with 20 results 'Parser by processes' 3338.16 ms
    async_parser.run()

    # check TODOs in other files
    # save results in csv file (with header)
    # Good, Price
    # Aspir, 14.99

    # * group goods by manufacturer
    # ** compare prices between pharmacies




