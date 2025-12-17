#pip install yfinance fastapi uvicorn requests

from fastapi import FastAPI, HTTPException
import yfinance as yf


app = FastAPI(title="YFinance Stock API", version="1.0")

@app.get("/current_price/{ticker}")
def get_company_info(ticker:str) :
    """
    Docstring for get_company_info
    
    :param ticker: Description
    :type ticker: str
    """
    try:
        company = yf.Ticker(ticker)
        info = company.info
        relevant_info = {
            "ticker": ticker,
            "shortName": info.get("shortName"),
            "longName": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "website": info.get("website"),
            "marketCap": info.get("marketCap"),
        }
        return relevant_info
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))