
pip install -r requirements.txt

# 1. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
uvicorn app.main:app --reload



# YFinance Stock API

A FastAPI app to get stock info from Yahoo Finance.

## Installation
pip install yfinance fastapi uvicorn requests

## Running the App
uvicorn yahoo_api:app --reload

## API Endpoints

### Get Company Info
- **Endpoint**: [GET /current_price/{ticker}](http://_vscodecontentref_/1)
- **Example**: Get info for Apple (AAPL)

  ```bash
  curl "http://127.0.0.1:8000/current_price/AAPL"

# YFinance Stock API

A FastAPI app to get stock info from Yahoo Finance.

## Installation
pip install yfinance fastapi uvicorn requests

## Running the App
uvicorn stock_api:app --reload  # For the new /stock endpoint
# Or uvicorn yahoo_api:app --reload  # For the old /current_price endpoint

## API Endpoints

### Get Stock Data (New Endpoint)
- **Endpoint**: `GET /stock/{ticker}`
- **Description**: Fetches current stock data like price, exchange, and currency.
- **Example**: Get data for Tesla (TSLA)

  ```bash
  curl "http://127.0.0.1:8000/stock/TSLA"