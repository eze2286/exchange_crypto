from fastapi import APIRouter
from routers.conecction_db import select_saldo_exchange, add_compras_database, add_saldo_database
from routers.schemas import Compra
from routers.external_data import close_price


router = APIRouter()
cierre = float(close_price)

@router.post("/compra")
def compra(compra:Compra):
    saldo = select_saldo_exchange()    
    monto_compra = float(compra.cantidad * cierre)
    if monto_compra > float(saldo):
        return {"error":f"Saldo insuficiente, su saldo es {saldo} y el monto de compra es {monto_compra}"}
    add_compra = add_compras_database(compra = compra)
    ajuste_saldo = add_saldo_database(monto_compra * -1.0)
    return compra