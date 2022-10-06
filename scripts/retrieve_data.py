#!/usr/bin/env python3

# Script modified from tutorial here: https://towardsdatascience.com/getting-rich-quick-with-machine-learning-and-stock-market-predictions-696802da94fe
# 2022-10-01

# Program description and version
desctext = 'retrieve_data.py: use AlphaVantage stock API to pull stock data and store for analysis.'
vers='retrieve_data.py v0.1'

# Parse inputs or provide help
import argparse, sys, json, time, os, pprint
import datetime as dt
from alpha_vantage.timeseries import TimeSeries

# Define date string, get script working directory
date_now_notime = time.strftime("%Y-%m-%d")
workdir = os.getcwd()

# Initialize parser
parser = argparse.ArgumentParser(description=desctext)
parser.add_argument("-t", "--ticker", help="Ticker abbreviation (e.g. AMZN, required)", type=str, metavar="", required=True)
parser.add_argument("-d", "--data_type", help="Data type to retrieve (daily, daily_adj (p), intraday or intraday_ext; default=daily)", choices=["daily", "adj_daily", "intraday", "intraday_ext"], type=str, metavar="", default="daily")
parser.add_argument("-v", "--version", help="show program version", action="version", version=vers)
parser.add_argument("-V", "--verbose", help="increase output verbosity", action="store_true")

# Print help if no arguments supplied
if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)

# Read arguments from the command line and provide useful feedback
args = parser.parse_args()
if args.verbose:
    print("Verbosity turned on")

# Parse inputs and set ticker to uppercase if lowercase was entered
ticker = args.ticker.upper()
dtype = args.data_type
ticker_data_filename = os.path.join(f"../data/{ticker}_{date_now_notime}_{dtype}.csv")
time_window = dtype

# Print important model parameters
print("Ticker symbol:", ticker)
print("Data type:", dtype)

# Retrieve data function
def save_dataset(symbol, time_window):
    credentials = json.load(open('creds.json', 'r'))
    api_key = credentials['av_api_key']
    print(symbol, time_window)
    ts = TimeSeries(key=api_key, output_format='pandas')
    if time_window == 'intraday':
        data, meta_data = ts.get_intraday(symbol, interval='1min', outputsize='full')
    elif time_window == 'daily':
        data, meta_data = ts.get_daily(symbol, outputsize='full')
    elif time_window == 'adj_daily':
        data, meta_data = ts.get_daily_adjusted(symbol, outputsize='full')
    elif time_window == 'intraday_ext':
        data, meta_data = ts.get_time_series_intraday_extended(symbol, interval='15min')

    data.to_csv(ticker_data_filename)

save_dataset(ticker, dtype)
    
