from fastapi import APIRouter
from routers.conecction_db import select_purchase_cripto, select_quantity_cripto, select_price_quantity_pond, add_sales_database, add_saldo_database
from routers.schemas import Venta
from routers.external_data import close_price


router = APIRouter()
cierre = float(close_price)

@router.post("/venta")
def venta(venta:Venta):
    compras = select_purchase_cripto()
    if len(compras)==0:
        return {"error":"No hay stock disponible para la venta"}
    cantidad = select_quantity_cripto()
    if venta.cantidad > cantidad:
        return {"error":f"Cantidad disponible: {str(cantidad)} - Cantidad solicitada: {str(venta.cantidad)}"}
    precio_compra_ponderado = select_price_quantity_pond()
    add_sale = add_sales_database(venta=venta)
    monto_venta = float(venta.cantidad * cierre)
    ajuste_saldo = add_saldo_database(monto_venta)
    
    print(monto_venta)
    print(precio_compra_ponderado)
    print(venta.cantidad)
    print(precio_compra_ponderado * venta.cantidad)
    resultado = monto_venta - (precio_compra_ponderado * venta.cantidad)
    return {"Se realizó la siguiente venta":venta,
            "El precio unitario de venta fue de U$S":cierre,
            "El precio promedio ponderado unitario de compra fue de U$S":precio_compra_ponderado,  
            "El resultado de la misma fue U$S":resultado}