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