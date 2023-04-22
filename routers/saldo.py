
from fastapi import APIRouter
from fastapi import status
from fastapi.responses import JSONResponse
from routers.conecction_db import select_saldo_exchange


router = APIRouter()

@router.get("/saldo",
            status_code=status.HTTP_200_OK,
            summary="Obtención del saldo actual en la cuenta", 
            tags=["Precio y Saldos"]
            )
async def saldo():
    saldo = select_saldo_exchange()   
    return JSONResponse({"Su saldo actual es U$D": str(saldo)})