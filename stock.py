from time_utils import *


class Stock:
    """@brief A Simple object used to represent a single Stock object.

         """

    def __init__(self, ticker):
        """
        A simple constructor used to initialize the stock object with a ticker

        :param self: The self class
            """
        self.ticker = ticker
        self.timestamp = get_time_in_std_format()
        self.current_price = 0.0
