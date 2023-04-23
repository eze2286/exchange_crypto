from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from routers.conecction_db import delete_registers_on_tables

router = APIRouter()

@router.delete("/reset_wallet",
            status_code=status.HTTP_200_OK,
            summary="Realizar el reseteo de la billetera, volviendo los saldos a 0", 
            tags=["Restauración"])
async def reset_wallet():
    """Vuelve a 0 tu cuenta y permite vovler a empezar el proceso para el caso de querer iniciar de nuevo"""
    try:
        reset = delete_registers_on_tables()
        return {"Operacion realizada satisfactoriamente: ": reset}
            
    except:
        HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                      detail="No se pudo resetar la billetera")