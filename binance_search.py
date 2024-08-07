import pandas as pd
import os
import time
from binance.client import Client
from datetime import timedelta, datetime
import numpy as np

binance_api_key = os.environ.get('BINANCE_API_KEY')
binance_api_secret = os.environ.get('BINANCE_SECRET')
binance_client = Client(api_key=binance_api_key, api_secret=binance_api_secret)

klines = binance_client.get_historical_klines('BNBBTC', Client.KLINE_INTERVAL_1HOUR, "27 Nov, 2021 00:00:00","27 Nov, 2021 00:03:00")

print(klines)
