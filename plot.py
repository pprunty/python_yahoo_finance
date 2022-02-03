import argparse
import os
import custom_logger

from time import sleep
from gplot import *

logging = custom_logger.init_logger()

# Instantiate data directorY
STOCK_DIR = os.path.dirname(os.path.realpath(__file__)) + "/data/"


def next_directory(index, base_directory):
    """
    @brief A function which gives the next file/directory in a given base_directory and index (file/directory) name

    :param index: The index file/directory name
    :param base_directory: The base directory where the index file exists
            """

    # Get a list of all directories/files in the given base directory path
    dir_list = os.listdir(base_directory)

    # Sort the files (this puts any file beginning with '.' at the bottom and assumes directory structure is standard.
    dir_list.sort()

    # Get next directory/file given the index
    next_dir = dir_list.index(index) + 1

    # If this next directory returns 0 or it is the last file in the directory, return None
    if next_dir == 0 or next_dir == len(dir_list):
        return None

    # Return the name of next directory/file in the base directory path
    return str(dir_list[next_dir])


def get_directory_offset(index, base_directory, offset):
    """
    @brief A function which gives the next file/directory in a given base_directory and index (file/directory) name

    :param index: The index file/directory name
    :param base_directory: The base directory where the index file exists
            """

    # Get a list of all directories/files in the given base directory path
    dir_list = os.listdir(base_directory)

    # Sort the files (this puts any file beginning with '.' at the bottom and assumes directory structure is standard.
    dir_list.sort()

    # Get next directory/file given the index
    five_back = dir_list.index(index) - offset

    # Return the name of next directory/file in the base directory path
    return str(dir_list[five_back])


def get_stock_prices(start, end, tickers, directory=STOCK_DIR):
    """
    @brief A function which iterates through the given directory, reads the data from each file in the specified
    directory and stores the data in an array.

    :param args: The command line arguments
    :param directory: The base directory where to search for the files
    :return array: The array containing data from start filename -> end filename
            """

    tickers = tickers.split()
    stock_data = []
    for ticker in tickers:
        # Initialize an empty array
        array = []

        # Get the current filename, and the end filename
        current_filename = directory + start + f"/{ticker}_{start}.txt"
        end_filename = directory + end + f"/{ticker}_{end}.txt"

        # Get the current (starting) directory
        current_directory = str(start)

        # While we haven't reached the end filename
        while current_directory != end:

            logging.info(f"Reading data from file {current_filename} into array.")

            # Open the file in the current directory
            with open(current_filename) as file:
                # Append data to the data array
                while line := file.readline().rstrip():
                    array.append(float(line))
                # Close file
                file.close()
            # Update current directory to be the next directory in the base directory
            current_directory = next_directory(current_directory, directory)
            # Update current filename to be the file in the updated current directory
            current_filename = directory + current_directory + f"/{ticker}_{current_directory}.txt"

        # Read data from the last file
        if os.path.isfile(end_filename):
            with open(end_filename) as file:
                while line := file.readline().rstrip():
                    array.append(float(line))
                file.close()
            stock_data.append(array)
        else:
            return []

    return stock_data


def get_average_array(stock_prices):
    """
    @brief A function which iterates through the given stock price array and returns a moving average array
    correlated to the given data.

    :param stock_prices: An array containing stock prices
    :return average_array: An array containing the moving average prices
            """
    average_array = []

    index = 1
    summation = 0.0
    for price in stock_prices:
        summation += float(price)
        average_array.append(summation / index)
        index += 1

    return average_array


def get_moving_average_dict(stock_prices):
    """
    @brief A function which iterates through the given stock price array and returns a moving average array
    correlated to the given data.

    :param stock_prices: An array containing stock prices
    :return average_array: An array containing the moving average prices
            """
    count = 0
    summation = 0.0
    for price in stock_prices:
        summation += float(price)
        count += 1

    return {'total': summation, 'count': count}


def plot_data(args):
    """
    @brief A function which uses GNUPLOT to plot data.

    :param args: The given command line arguments
            """

    tickers = args.ticker.split()

    # Get stock price array
    stock_prices = get_stock_prices(args.start, args.end, args.ticker)

    # Set title to plot using the ticker
    gplot.title(f'"{args.ticker}"').grid()

    # Set xlabel title
    xlabel = f'"Time: {args.start.replace("_", "/")}  - {args.end.replace("_", "/")}"' if args.start != args.end else f'"Time {args.start.replace("_", "/")}"'
    gplot.xlabel(xlabel)
    gplot.mxtics().mytics(2)

    gplot.key("bottom right")

    if len(tickers) == 2:
        gplot(get_stock_prices(args.start, args.end, tickers[0]), " axes x1y1", f" w l t '{tickers[0]}'",
              ",",
              get_stock_prices(args.start, args.end, tickers[1]), " axes x1y2",
              f" w l t '{tickers[1]}'"
              )
    else:
        gplot(get_stock_prices(args.start, args.end, tickers[0]), " axes x1y1", f" w l t '{tickers[0]}'")


if __name__ == '__main__':
    """
        """
    parser = argparse.ArgumentParser(description='Program to store intra-day data on Stocks')
    parser.add_argument("-t", "--ticker", type=str, dest="ticker", help="The stock ticker(s). The capability to"
                                                                        "graph two stocks side by side is possible but"
                                                                        "you must put tickers in a string separated by"
                                                                        "a single space.", required=True)
    parser.add_argument("-s", "--start", type=str, dest="start", help="The start date of data. Format: YYYY_MM_DD")
    parser.add_argument("-e", "--end", type=str, dest="end", help="The end date of data. Format: YYYY_MM_DD")

    args = parser.parse_args()

    plot_data(args)
    sleep(120)
