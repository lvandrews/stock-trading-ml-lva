#!/usr/bin/env python3

# Script modified from tutorial here: https://towardsdatascience.com/getting-rich-quick-with-machine-learning-and-stock-market-predictions-696802da94fe
# 2022-10-01

# Program description and version
desctext = 'retrieve_data.py: use AlphaVantage stock API to pull stock data and store for analysis.'
vers='retrieve_data.py v0.1'

# Parse inputs or provide help
import argparse, sys, json, time, os
import datetime as dt
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
#import json
#import time
#import os

# Define date strings
#today=dt.date.today()
#year_ago=today - dt.timedelta(days=365)
#date_now = time.strftime("%Y-%m-%d_%H-%M-%S")
date_now_notime = time.strftime("%Y-%m-%d")
#dt_string = time.strftime("%b-%d-%Y %I:%M:%S %p")

# Initialize parser
parser = argparse.ArgumentParser(description=desctext)
parser.add_argument("-t", "--ticker", help="Ticker abbreviation (e.g. AMZN, required)", type=str, metavar="", required=True)
parser.add_argument("-d", "--data_type", help="Data type to retrieve (daily, daily_adj, or intraday; default=daily)", choices=["daily", "adj_daily", "intraday"], type=str, metavar="", default="daily")
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
#parser.parse_args()
ticker = args.ticker.upper()
#data_type = args.data_type()
#print(ticker)
#print(args.data_type)
dtype = args.data_type
#print(dtype)
#print(data_type)
#print(vars(args))



#quit()
# Print important model parameters
print("Ticker symbol:", ticker)

print("Data type:", dtype)
#print("Epochs to train:", args.epoch)
#print("Test size:", args.test_size)
#print("Window size:", args.window_size)
#print("Lookup step:", args.lookup_step)
#print("RNN cell: LSTM")

# Ticker data filename
ticker_data_filename = os.path.join(f"{ticker}_{date_now_notime}_{dtype}.csv")

print("Output file here:", ticker_data_filename)
def save_dataset(ticker, dtype):
    credentials = json.load(open('creds.json', 'r'))
    api_key = credentials['av_api_key']
    ts = TimeSeries(key=api_key, output_format='pandas')
    if dtype == 'intraday':
        data, meta_data = ts.get_intraday(ticker, interval='1min', outputsize='full')
    elif dtype == 'daily':
       data, meta_data = ts.get_daily(ticker, outputsize='full')
    elif dtype == 'daily_adj':
        data, meta_data = ts.get_daily_adjusted(ticker, outputsize='full')

    pprint(data.head(10))

    data.to_csv(ticker_data_filename)


#if __name__ == "__main__":
#    parser = argparse.ArgumentParser()

#    parser.add_argument('symbol', type=str, help="the stock symbol you want to download")
#    parser.add_argument('time_window', type=str, choices=[
#                        'intraday', 'daily', 'daily_adj'], help="the time period you want to download the stock history for")

    namespace = parser.parse_args()
    save_dataset(**vars(namespace))
    
