import math
import time
import requests
import custom_logger

from time_utils import *
logger = custom_logger.init_logger()


def get_current_price(stock):
    """
    A function which uses Yahoo finance API to query data and web scrape live prices into trading program

        """
    try:

        # Url for Yahoo query
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock.ticker}"

        # Get the time today when the markets open
        date_time = get_open_time_in_std_format()

        pattern = '%Y-%m-%d %H:%M:%S'
        start_seconds = int(time.mktime(time.strptime(date_time, pattern)))

        end_seconds = int(time.time())

        params = {
            "period1": start_seconds,
            "period2": end_seconds,
            "interval": "1d",
            "events": "div,splits"
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }

        resp = requests.get(url, params=params, headers=headers)

        if not resp.ok:
            raise AssertionError(resp.json())

        data = resp.json()

        close_price = data['chart']['result'][0]['indicators']['quote'][0]['close'][0]

        price = float(close_price)

        # Check that the price is a valid datatype
        if not math.isnan(price):
            stock.timestamp = get_time_in_std_format()
            stock.current_price = price
            return stock
        else:
            logger.warning(f"{get_time_in_std_format()} Data for ticker {stock.ticker} returned NaN")
            return stock

    except Exception as e:

        # Log exception
        logger.warning(f" {e} - Missing data for ticker {stock.ticker} at {get_time_in_std_format()}."
                       f" Using previous value: {stock.current_price}")

        # Return previously scrapped stock data
        return stock
