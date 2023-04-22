from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Body
from fastapi.responses import JSONResponse
from routers.conecction_db import select_saldo_exchange, add_compras_database, add_saldo_database
from routers.schemas import Compra
from routers.external_data import close_price

router = APIRouter()

@router.post("/compra",
            status_code=status.HTTP_201_CREATED,
            summary="Realizar una compra de la cripto indicando la cantidad requerida", 
            tags=["Compras y Ventas"])
async def compra(
    compra:Compra = Body(...,
                         description="Ingresar la cantidad que desea comprar"                         
                         )
                         ):
    try:
        cierre = float(close_price)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= "No se pudo obtener el precio actual")
    saldo = select_saldo_exchange()
    if compra.cantidad == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= ("La cantidad comprada debe ser mayor a 0"))    
    monto_compra = float(compra.cantidad * cierre)
    if monto_compra > float(saldo):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"error: Saldo insuficiente, su saldo es {saldo} y el monto de compra es {monto_compra}")        
    add_compra = add_compras_database(compra = compra)
    ajuste_saldo = add_saldo_database(monto_compra * -1.0)
    return JSONResponse(
        {"Success operation": f"se realizó la compra de {str(compra.cantidad)} unidades"})