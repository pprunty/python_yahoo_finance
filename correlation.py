# import pandas
from time import sleep

import numpy as np
import pandas as pd

from numpy import cov
import config
import plot
import sys
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", None, "display.max_columns", None)

if __name__ == '__main__':

    tickers = config.stocks

    start_date = "2022_02_01"
    end_date = "2022_02_03"

    data = {}
    for ticker in tickers:
        data[ticker] = plot.get_stock_prices(start_date, end_date, ticker)

    # creation of DataFrame
    df = pd.DataFrame(data)

    print(df)

    # creation of correlation matrix
    corrM = df.corr()

    print(corrM)

    fig = plt.figure(figsize=(30, 12))
    # # Store heatmap object in a variable to easily access it when you want to include more features (such as title).
    # # Set the range of values to be displayed on the colormap from -1 to 1, and set the annotation to True to display the correlation values on the heatmap.
    # heatmap = sns.heatmap(corrM, cmap="Blues", vmin=-1, vmax=1, annot=True)
    # # Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
    # heatmap.set_title('Correlation Heatmap', fontdict={'fontsize': 10}, pad=12)

    mask = np.triu(np.ones_like(corrM, dtype=bool))
    heatmap = sns.heatmap(corrM, mask=mask, vmin=-1, vmax=1, annot=True, cmap='BrBG')
    heatmap.set_title('Triangle Correlation Heatmap', fontdict={'fontsize': 18}, pad=16)

    fig.savefig('my_figure.png')

    # # Get stock prices for 1 day
    # MSFT = plot.get_stock_prices(start_date, start_date, "MSFT")
    # DJI = plot.get_stock_prices(start_date, start_date, "^DJI")
    #
    # # Get average for stock prices
    # MSFT_mu = sum(MSFT) / len(MSFT)
    # DJI_mu = sum(DJI) / len(DJI)
    #
    # MSFT_DJI_r = cov(MSFT, DJI)
    #
    # 2
    #


