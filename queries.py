from schemas import Compra, Venta, Saldo
from datetime import date, datetime
from database import get_connection_to_data_base
from external_data import close_price
from typing import Union


def add_saldo_database(saldo_exchange:Union[Saldo, float]):
    if type(saldo_exchange)==Saldo:
        saldo_exchange = saldo_exchange.saldo
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    cursor.execute("""
        INSERT INTO saldo_exchange (saldo, date) VALUES (?, ?)
    """, (saldo_exchange, datetime.now()))
    con_db.commit()
    con_db.close()

def select_saldo_exchange():
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    cursor.execute("""
        SELECT SUM(saldo) FROM saldo_exchange WHERE date <= ?
    """, (datetime.now(),))
    saldo = cursor.fetchall()[0][0]    
    con_db.close()
    return saldo

def add_compras_database(compra:Compra):
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    cursor.execute("""
        INSERT INTO compras (cantidad, precio, date) VALUES (?, ?, ?)
    """, (compra.cantidad, close_price, datetime.now()))
    con_db.commit()
    con_db.close()

def add_sales_database(venta:Venta):
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    cursor.execute("""
        INSERT INTO ventas (cantidad, precio, date) VALUES (?, ?, ?)
    """, (venta.cantidad, close_price, datetime.now()))
    con_db.commit()
    con_db.close()

def select_purchase_cripto():
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    cursor.execute("""
        SELECT * FROM compras WHERE date <= ?
    """, (datetime.now(),))
    compras = cursor.fetchall()    
    con_db.close()
    return compras

def select_quantity_cripto():
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    cursor.execute("""
        SELECT SUM(cantidad) FROM compras WHERE date <= ?
    """, (datetime.now(),))
    cantidad = cursor.fetchall()[0][0]    
    con_db.close()
    return cantidad

def select_price_quantity_pond():
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    cursor.execute("""
        SELECT 
           (SUM(cantidad) OVER(PARTITION BY date)/(SELECT SUM(cantidad) from compras))*precio
           FROM compras WHERE date <= ?
    """, (datetime.now(),))
    precios_ponderados = cursor.fetchall()
    sum_precio_ponderado  = 0
    for precio in precios_ponderados:
        sum_precio_ponderado += precio[0]
    con_db.close()
    return sum_precio_ponderado

# test = select_price_quantity_pond()
# print(test)