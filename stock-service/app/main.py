from fastapi import FastAPI
from app.routers import stock, company

app = FastAPI(
    title="Stock & Company Data API",
    description="Unified API for stock prices and company information using Yahoo Finance",
    version="1.0.0"
)

app.include_router(stock.router)
app.include_router(company.router)
