import yfinance as yf


def get_stock_info(ticker: str) -> dict:
    stock = yf.Ticker(ticker)
    info = stock.info

    if not info or "regularMarketPrice" not in info:
        raise ValueError("Invalid ticker or data unavailable")

    return info


def get_company_profile(ticker: str) -> dict:
    info = get_stock_info(ticker)

    return {
        "symbol": info.get("symbol"),
        "shortName": info.get("shortName"),
        "longName": info.get("longName"),
        "industry": info.get("industry"),
        "sector": info.get("sector"),
        "country": info.get("country"),
        "website": info.get("website"),
        "description": info.get("longBusinessSummary")
    }
