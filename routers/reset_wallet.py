from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from routers.conecction_db import delete_registers_on_tables

router = APIRouter()

@router.delete("/reset_wallet",
            status_code=status.HTTP_205_RESET_CONTENT,
            summary="Realizar el reseteo de la billetera, volviendo los saldos a 0", 
            tags=["Restauración"])
async def reset_wallet():
    try:
        reset = delete_registers_on_tables()
        return JSONResponse(
            {"Operacion realizada satisfactoriamente: ": reset})
    except:
        HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                      detail="No se pudo resetar la billetera")