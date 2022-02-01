import config
import random

from time import sleep
from stock import Stock
from data import Data
from yahoo_finance import *

if __name__ == '__main__':

    stocks = []
    data = Data()

    for ticker in config.stocks:
        stocks.append(Stock(ticker))

    # Check if the markets are open or not
    market_is_open = True if 930 <= int(get_time_in_hr_mins()) <= 1600 else False

    while market_is_open:

        for stock in stocks:
            stock = get_current_price(stock)

        data.write_stock_data_to_file(stocks)
        # Sleep 30 seconds, prices are updated on a intra-minute basis
        logger.info(f"Finished writing stock data to files with timestamp: {get_time_in_std_format()}")
        sleep(30)

        # Shuffle stocks to prevent scrapping prices in the same order every minute
        random.shuffle(stocks)

        # Check if market is still open
        market_is_open = True if 930 <= int(get_time_in_hr_mins()) <= 1600 else False
