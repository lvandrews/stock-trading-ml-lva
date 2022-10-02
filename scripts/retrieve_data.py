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
parser.add_argument("-d", "--data-type", help="Data type to retrieve (daily, daily_adj, or intraday, default=daily)", type=str, choices=['intraday', 'daily', 'daily_adj'], default="daily")
#parser.add_argument("-e", "--epoch", help="Epochs to train (integer, default = 5)", type=int, metavar='', default="5")
#parser.add_argument("-s", "--test_size", help="Test ratio size, 0.2 is 20%% (decimal, default = 0.2)", type=float, metavar='', default="0.2")
#parser.add_argument("-w", "--window_size", help="Window length used to predict (integer, default = 50)", type=int, metavar='', default="50")
#parser.add_argument("-l", "--lookup_step", help="Lookup step, 1 is the next day (integer, default = 5)", type=int, metavar='', default="5")
#parser.add_argument("-b", "--begin_date", help="Beginning date for analysis set (e.g. 2021-04-20, default = one year ago from present date)", type=str, metavar='', default=year_ago)
#parser.add_argument("-a", "--all_time", help="Use all available data (supercedes -b)", action="store_true")
#parser.add_argument("-k", "--keep_results", help="Keep output dataframe (saves as .csv to results directory)", action="store_true")

parser.add_argument("-v", "--version", help="show program version", action="version", version="%(prog)s 0.1")
parser.add_argument("-V", "--verbose", help="increase output verbosity", action="store_true")

# Print help if no arguments supplied
if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)

# Read arguments from the command line and provide useful feedback
args = parser.parse_args()
if args.verbose:
    print("Verbosity turned on")
    
parser.parse_args()

# Set ticker symbol to uppercase if lowercase was entered
ticker = args.ticker.upper()

# Print important model parameters
print("Ticker symbol:", ticker)
#print("Epochs to train:", args.epoch)
#print("Test size:", args.test_size)
#print("Window size:", args.window_size)
#print("Lookup step:", args.lookup_step)
#print("RNN cell: LSTM")

def save_dataset(ticker, time_window):
    credentials = json.load(open('creds.json', 'r'))
    api_key = credentials['av_api_key']
    print(ticker, time_window)
    ts = TimeSeries(key=api_key, output_format='pandas')
    if time_window == 'intraday':
        data, meta_data = ts.get_intraday(ticker, interval='1min', outputsize='full')
    elif time_window == 'daily':
        data, meta_data = ts.get_daily(ticker, outputsize='full')
    elif time_window == 'daily_adj':
        data, meta_data = ts.get_daily_adjusted(ticker, outputsize='full')

    pprint(data.head(10))

    data.to_csv(f'../data/{ticker}_{time_window}.csv')


#if __name__ == "__main__":
#    parser = argparse.ArgumentParser()

#    parser.add_argument('symbol', type=str, help="the stock symbol you want to download")
#    parser.add_argument('time_window', type=str, choices=[
                        'intraday', 'daily', 'daily_adj'], help="the time period you want to download the stock history for")

#    namespace = parser.parse_args()
#    save_dataset(**vars(namespace))
    
