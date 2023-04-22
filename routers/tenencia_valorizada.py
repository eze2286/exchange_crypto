from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from routers.conecction_db import select_valued_possesion


router = APIRouter()


@router.get("/tenencia_valorizada",
            status_code=status.HTTP_200_OK,
            summary="Obtención de la tenencia actual de la criptomoneda valorizada de acuerdo al precio promedio ponderado de compra", 
            tags=["Precio y Saldos"]
            )
async def tenencia():
    tenencia = select_valued_possesion()
    if not tenencia:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No es posible realizar la transacción ya que no registra tenencias a la fecha")
    return JSONResponse (
            {"Tenencia actual  ":f"{str(tenencia[0])} unidades",
            "Tenencia actual valorizada ":f"{str(tenencia[1])}"})