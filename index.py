from modules import binance
from settings import settings

for currency in settings.config['currency']:
    binance.thread_check_currency_price_change(currency, settings.config['timeout'])
