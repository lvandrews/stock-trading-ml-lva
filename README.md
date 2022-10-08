# Stock Trading with Machine Learning

## Forked by Lela

Making the following updates:
1. Adding argparse parser to commands (in progress 2022-10-07)
2. Organize files (done 2022-10-02)
    ./data: Downloaded data files go here
    ./docs: Any useful documents here
    ./install: List of python3 packages to be install via pip
    ./models: Machine learning models to be made available via main script
    ./scripts: Core scripts to process the analysis of a stock
2. Improving data retrieval
    a. Save to data folder (done)
    b. Tag files with date of retrieval (done)
    c. Check if file exists to avoid unnecessary API calls
    d. Permit alternative data sources
3. Improve file structure
    a. Add shebang and set executable status
4. Add install script that chooses the correct tensorflow based on your system
5. Add script to build credential file
6. Add new models with additional data types
7. Build installer that will work on Windows (Linux only for now)

## Overview

A stock trading bot that uses machine learning to make price predictions.

## Requirements

-   Python 3.5+
-   alpha_vantage
-   pandas
-   numpy
-   sklearn
-   keras
-   tensorflow
-   matplotlib

## Documentation

[Blog Post](https://yacoubahmed.me/blog/stock-prediction-ml)

[Medium Article](https://medium.com/towards-data-science/getting-rich-quick-with-machine-learning-and-stock-market-predictions-696802da94fe)

## Train your own model

1. Clone the repo
2. Pip install the requirements `pip install -r requirements.txt`
3. Save the stock price history to a csv file `python save_data_to_csv.py --help`
4. Edit one of the model files to accept the symbol you want
5. Edit model architecture
6. Edit dataset preprocessing / history_points inside util.py
7. Train the model `python tech_ind_model.py` or `python basic_model.py`
8. Try the trading algorithm on the newly saved model `python trading_algo.py`

## License

[GPL-3.0](https://www.gnu.org/licenses/quick-guide-gplv3.html)
