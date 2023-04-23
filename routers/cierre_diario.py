
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from routers.external_data import close_price


router = APIRouter()
@router.get("/cierre_diario",
            status_code=status.HTTP_200_OK,
            summary="Obtención del precio actual de la cripto", 
            tags=["Precio y Saldos"])
async def cierre_diario():
    """Obtención del precio actual de la criptomoneda"""
    try:
        cierre = round(float(close_price), 3)
        return JSONResponse({"El precio actual es de U$S":cierre})
    except:
        HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                      detail="No se pudo obtener el precio")