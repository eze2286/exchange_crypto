from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Body
from routers.conecction_db import add_saldo_database
from routers.schemas import Saldo


router = APIRouter()

@router.post("/saldo",
            status_code=status.HTTP_201_CREATED,
            summary = "Agregar saldo a la billetera", 
            tags=["Precio y Saldos"])
async def add_saldo(
    saldo:Saldo = Body(...,
                       description="Ingresar el saldo a cargar en la billetera")
    ):
    if saldo.saldo == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="El saldo a ingresar debe ser mayor a 0")
    saldo_exch = add_saldo_database(saldo_exchange = saldo)
    
    return {"Transaccion satisfactoria":f"Se cargaron correctamente U$S {str(saldo.saldo)} a su billetera"}