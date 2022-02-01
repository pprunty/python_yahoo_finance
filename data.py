import os
import config
import custom_logger

from time_utils import *

logger = custom_logger.init_logger()


class Data:
    """
    @brief The Data class used for Dow Surfer to write live data to files.

        """

    def __init__(self):
        """
        @brief A constructor for the Data class. This class creates directories each day to record
        data such as stock prices, strategy target prices and portfolio performance.

            """
        # Get date for file formatting
        self.date = str(get_time_in_file_std_format())

        # Parent directory
        self.parent_dir = os.path.dirname(os.path.realpath(__file__))

        # Stock directory
        self.stock_dir = "data/" + self.date
        self.create_dir(self.stock_dir)

    def create_dir(self, directory):
        """
        @brief A function which creates a directory, using the absolute path of the
        parent directory, instantiated in the constructor.

        :param directory: The directory to be created.
        :param self: The Portfolio class
            """
        try:
            path = os.path.join(str(self.parent_dir), directory)
            os.makedirs(path)
        except Exception as e:
            logger.critical(e)

    def write_stock_data_to_file(self, stocks):
        """
        @brief A function used to write intra minute stock data to a file using a trade book. The file format will be
        /<parent_path>/<stock_dir>/<ticker>_<trade_object_id>_<date>.txt

        :param stocks: The list of stocks
            """
        try:
            for stock in stocks:
                filename = str(self.parent_dir + "/" + self.stock_dir + f"/{stock.ticker}_{self.date}.txt")
                with open(filename, "a+") as f:
                    f.write(f"{stock.current_price}\n")
                    f.close()
        except Exception as e:
            logger.critical(e)
