from fastapi import FastAPI
import pandas as pd
from schemas import Compra, Venta, Saldo
from datetime import date
#from queries import add_compras_database, select_purchase_cripto, select_quantity_cripto,add_sales_database, add_saldo_database, select_saldo_exchange, select_price_quantity_pond
from conecction_db import add_compras_database, select_purchase_cripto, select_quantity_cripto,add_sales_database, add_saldo_database, select_saldo_exchange, select_price_quantity_pond, select_valued_possesion

from external_data import close_price

cierre = float(close_price)


app = FastAPI()
# saldo_actual = SaldoInicial()
###########################
@app.get("/cierre_diario")
def cierre_diario():
    return cierre
###########################
@app.get("/saldo")
def saldo():
    saldo = select_saldo_exchange()
    return {"Su saldo actual es ": str(saldo)}
###########################
@app.get("/tenencia_valorizada")
def tenencia():
    tenencia = select_valued_possesion()
    return {"Tenencia actual  ":f"{str(tenencia[0])} unidades",
            "Tenencia actual valorizada ":f"{str(tenencia[1])}"}
###########################
@app.post("/saldo")
def add_saldo(saldo:Saldo):
    saldo_exch = add_saldo_database(saldo_exchange = saldo)
    return {"Transaccion satisfactoria":f"Se cargaron correctamente U$S {str(saldo.saldo)} a su billetera"}
###########################
@app.post("/compra")
def compra(compra:Compra):
    saldo = select_saldo_exchange()    
    monto_compra = float(compra.cantidad * cierre)
    if monto_compra > float(saldo):
        return {"error":f"Saldo insuficiente, su saldo es {saldo} y el monto de compra es {monto_compra}"}
    add_compra = add_compras_database(compra = compra)
    ajuste_saldo = add_saldo_database(monto_compra * -1.0)
    
    return compra
##################################
@app.post("/venta")
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
    return {"Se realizó la siguiente venta":venta, "El resultado de la misma fue U$S ":resultado}
####################################
