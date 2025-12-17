from fastapi import APIRouter, HTTPException
from app.services.yahoo_service import get_stock_info

router = APIRouter(
    prefix="/stock",
    tags=["Stock Market"]
)


@router.get("/{ticker}")
def get_stock_data(ticker: str):
    """
    Fetch real-time stock market data
    """
    try:
        info = get_stock_info(ticker)

        return {
            "symbol": info.get("symbol"),
            "exchange": info.get("exchange"),
            "currency": info.get("currency"),
            "currentPrice": info.get("regularMarketPrice"),
            "previousClose": info.get("previousClose"),
            "open": info.get("regularMarketOpen"),
            "dayHigh": info.get("dayHigh"),
            "dayLow": info.get("dayLow"),
            "volume": info.get("volume"),
            "marketCap": info.get("marketCap"),
        }

    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
