from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Body
from fastapi.responses import JSONResponse
from routers.conecction_db import select_purchase_cripto, select_quantity_cripto, select_price_quantity_pond, add_sales_database, add_saldo_database
from routers.schemas import Venta
from routers.external_data import close_price


router = APIRouter()

@router.post("/venta",
            status_code=status.HTTP_201_CREATED,
            summary="Realizar una venta de la cripto indicando la cantidad requerida", 
            tags=["Compras y Ventas"])
async def venta(
    venta:Venta = Body(...,
                       description = "Ingresar la cantidad que desea vender")
    ):
    try:
        cierre = float(close_price)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= "No se pudo obtener el precio actual")
    compras = select_purchase_cripto()
    if len(compras)==0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= "error: No hay stock disponible para la venta")
        
    cantidad = select_quantity_cripto()
    if venta.cantidad > cantidad:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= (f"error : Cantidad disponible: {str(cantidad)} - Cantidad solicitada: {str(venta.cantidad)}"))
    if venta.cantidad == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= ("La cantidad vendida debe ser mayor a 0")) 
    precio_compra_ponderado = select_price_quantity_pond()
    add_sale = add_sales_database(venta=venta)
    monto_venta = float(venta.cantidad * cierre)
    ajuste_saldo = add_saldo_database(monto_venta)
   
    resultado = monto_venta - (precio_compra_ponderado * venta.cantidad)
    return JSONResponse(
            {"Se realizó la siguiente venta":venta,
            "El precio unitario de venta fue de U$S":cierre,
            "El precio promedio ponderado unitario de compra fue de U$S":precio_compra_ponderado,  
            "El resultado de la misma fue U$S":resultado})