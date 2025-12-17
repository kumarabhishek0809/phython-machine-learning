from fastapi import APIRouter, HTTPException
from app.services.yahoo_service import get_company_profile

router = APIRouter(
    prefix="/company",
    tags=["Company Info"]
)


@router.get("/{ticker}")
def get_company_info(ticker: str):
    """
    Fetch company profile information
    """
    try:
        return get_company_profile(ticker)

    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
