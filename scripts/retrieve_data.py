#!/usr/bin/env python3

# Script modified from tutorial here: https://towardsdatascience.com/getting-rich-quick-with-machine-learning-and-stock-market-predictions-696802da94fe
# 2022-10-01

# Parse inputs or provide help
import argparse, sys
import datetime as dt
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import json

today=dt.date.today()
year_ago=today - dt.timedelta(days=365)

# Program description
desctext = 'retrieve_data.py: use AlphaVantage stock API to pull stock data and store for analysis.'

# Initialize parser
parser = argparse.ArgumentParser(description=desctext)

parser.add_argument("-t", "--ticker", help="Ticker abbreviation (e.g. AMZN, required)", type=str, metavar='', required=True)
parser.add_argument("-e", "--epoch", help="Epochs to train (integer, default = 5)", type=int, metavar='', default="5")
parser.add_argument("-s", "--test_size", help="Test ratio size, 0.2 is 20%% (decimal, default = 0.2)", type=float, metavar='', default="0.2")
parser.add_argument("-w", "--window_size", help="Window length used to predict (integer, default = 50)", type=int, metavar='', default="50")
parser.add_argument("-l", "--lookup_step", help="Lookup step, 1 is the next day (integer, default = 5)", type=int, metavar='', default="5")
parser.add_argument("-b", "--begin_date", help="Beginning date for analysis set (e.g. 2021-04-20, default = one year ago from present date)", type=str, metavar='', default=year_ago)
parser.add_argument("-a", "--all_time", help="Use all available data (supercedes -b)", action="store_true")
parser.add_argument("-k", "--keep_results", help="Keep output dataframe (saves as .csv to results directory)", action="store_true")

parser.add_argument("-v", "--version", help="show program version", action="version", version="%(prog)s 0.1")
parser.add_argument("-V", "--verbose", help="increase output verbosity", action="store_true")



def save_dataset(symbol, time_window):
    credentials = json.load(open('creds.json', 'r'))
    api_key = credentials['av_api_key']
    print(symbol, time_window)
    ts = TimeSeries(key=api_key, output_format='pandas')
    if time_window == 'intraday':
        data, meta_data = ts.get_intraday(
            symbol='MSFT', interval='1min', outputsize='full')
    elif time_window == 'daily':
        data, meta_data = ts.get_daily(symbol, outputsize='full')
    elif time_window == 'daily_adj':
        data, meta_data = ts.get_daily_adjusted(symbol, outputsize='full')

    pprint(data.head(10))

    data.to_csv(f'./{symbol}_{time_window}.csv')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('symbol', type=str, help="the stock symbol you want to download")
    parser.add_argument('time_window', type=str, choices=[
                        'intraday', 'daily', 'daily_adj'], help="the time period you want to download the stock history for")

    namespace = parser.parse_args()
    save_dataset(**vars(namespace))
