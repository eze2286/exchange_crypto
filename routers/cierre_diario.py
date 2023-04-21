
from fastapi import APIRouter
from routers.external_data import close_price



router = APIRouter()
cierre = float(close_price)


@router.get("/cierre_diario")
async def cierre_diario():
    return cierre