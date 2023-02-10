import time, ccxt, threading

exchange: ccxt.binance = ccxt.binance()

max_price: float = None

def thread_check_currency_price_change(currency: str, timeout: int) -> None:
    """
    The function starts a separate flow to view the change in currency prices, returns an alert to the console when the price changes by 1%

    :param currency: str, the currency to monitor.
    :param timeout: int, the number of seconds between each check.

    :return: None
    """
    def currency_price_change():
        global max_price
        while True:
            current_price: float = float(exchange.fetch_ticker(currency)['last'])

            if max_price is None or current_price > max_price:
                max_price = current_price
                
            if (max_price - current_price) / max_price >= 0.01:
                print(f'Currency: {currency} price fell 1%!')
            time.sleep(timeout)
    return threading.Thread(target = currency_price_change).start()