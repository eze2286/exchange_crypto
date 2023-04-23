
from fastapi import APIRouter
from fastapi import status
from routers.conecction_db import select_saldo_exchange


router = APIRouter()

@router.get("/saldo",
            status_code=status.HTTP_200_OK,
            summary="Obtención del saldo actual en la cuenta", 
            tags=["Precio y Saldos"]
            )
async def saldo():
    """Te permite saber tu saldo actual en dolares en la billetera"""
    saldo = select_saldo_exchange()
    if not saldo:
        saldo = 0.0   
    return {"Su saldo actual es U$D": str(saldo)}