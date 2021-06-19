from blockchain import exchangerates

ticker=exchangerates.get_ticker()
for k in ticker:
    print(k, ticker[k].p15min)