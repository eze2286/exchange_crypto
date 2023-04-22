from routers.schemas import Compra, Venta, Saldo
from datetime import date, datetime
#from database import get_connection_to_data_base
from routers.external_data import close_price
from typing import Union
import pymysql
import os

def get_connection_to_data_base():
    conn=pymysql.connect(
    host = 'exchange-db.cjgfmaah7lau.us-east-1.rds.amazonaws.com',
    user =  'admin',
    password = os.getenv('dbpassword'))       
    return conn

def add_saldo_database(saldo_exchange:Union[Saldo, float]):
    if type(saldo_exchange)==Saldo:
        saldo_exchange = saldo_exchange.saldo
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    sql_use = """USE exchange"""
    cursor.execute(sql_use)
    cursor.execute("""
        INSERT INTO saldo_exchange (saldo, date) VALUES (%s, %s)
    """, (saldo_exchange, datetime.now()))
    con_db.commit()
    con_db.close()

def select_saldo_exchange():
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    sql_use = """USE exchange"""
    cursor.execute(sql_use)
    cursor.execute("""
        SELECT SUM(saldo) FROM saldo_exchange WHERE date <= %s
    """, (datetime.now(),))
    saldo = cursor.fetchall()[0][0]    
    con_db.close()
    return saldo

def add_compras_database(compra:Compra):
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    sql_use = """USE exchange"""
    cursor.execute(sql_use)
    cursor.execute("""
        INSERT INTO compras (cantidad, precio, date) VALUES (%s, %s, %s)
    """, (compra.cantidad, close_price, datetime.now()))
    con_db.commit()
    con_db.close()

def add_sales_database(venta:Venta):
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    sql_use = """USE exchange"""
    cursor.execute(sql_use)
    cursor.execute("""
        INSERT INTO ventas (cantidad, precio, date) VALUES (%s, %s, %s)
    """, (venta.cantidad, close_price, datetime.now()))
    con_db.commit()
    con_db.close()

def select_purchase_cripto():
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    sql_use = """USE exchange"""
    cursor.execute(sql_use)
    cursor.execute("""
        SELECT * FROM compras WHERE date <= %s
    """, (datetime.now(),))
    compras = cursor.fetchall()    
    con_db.close()
    return compras

def select_quantity_cripto():
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    sql_use = """USE exchange"""
    cursor.execute(sql_use)
    cursor.execute("""
        SELECT SUM(cantidad) FROM compras WHERE date <= %s
    """, (datetime.now(),))
    cantidad = cursor.fetchall()[0][0]    
    con_db.close()
    return cantidad

def select_price_quantity_pond():
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    sql_use = """USE exchange"""
    cursor.execute(sql_use)
    cursor.execute("""
    SELECT c.cantidad * c.precio / t.total
    FROM compras c
    JOIN (
        SELECT SUM(cantidad) as total FROM compras WHERE date <= %s
    ) t
    WHERE c.date <= %s
""", (datetime.now(), datetime.now()))
    precios_ponderados = cursor.fetchall()
    sum_precio_ponderado  = 0
    for precio in precios_ponderados:
        sum_precio_ponderado += precio[0]
    con_db.close()
    return sum_precio_ponderado

def select_valued_possesion():
    cantidad_comprada = select_quantity_cripto()
    if not cantidad_comprada:
        return None
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    sql_use = """USE exchange"""
    cursor.execute(sql_use)
    cursor.execute("""
        SELECT SUM(cantidad) FROM ventas WHERE date <= %s
    """, (datetime.now(),))
    cantidad_vendida = cursor.fetchall()[0][0] 
    con_db.close()    
    if not cantidad_vendida:
        tenencia_cantidad = cantidad_comprada
    else:
        tenencia_cantidad = cantidad_comprada - cantidad_vendida
    tenencia_valorizada = tenencia_cantidad * close_price
    return tenencia_cantidad, tenencia_valorizada

def delete_registers_on_tables():
    con_db = get_connection_to_data_base()
    cursor = con_db.cursor()
    sql_use = """USE exchange"""
    cursor.execute(sql_use)
    cursor.execute("DELETE FROM saldo_exchange")
    cursor.execute("DELETE FROM compras")
    cursor.execute("DELETE FROM ventas")
    con_db.commit()
    con_db.close()
    return "Se ha reseteado correctamente toda la informacion de la billetera"  
# test = select_valued_possesion()
# print(test)

# conexion = get_connection_to_data_base()
# cursor=conexion.cursor()
# sql_use = """USE exchange"""
# cursor.execute(sql_use)
# sql_query = """SELECT * FROM compra"""
# cursor.execute(sql_query)
# data = cursor.fetchall()
# print(data)

# conexion = get_connection_to_data_base()
# cursor=conexion.cursor()
# sql_use = """USE exchange"""
# cursor.execute(sql_use)
# cursor.execute("""
#     SELECT c.cantidad * c.precio / t.total
#     FROM compras c
#     JOIN (
#         SELECT SUM(cantidad) as total FROM compras WHERE date <= %s
#     ) t
#     WHERE c.date <= %s
# """, (datetime.now(), datetime.now()))


# sql_query = """SELECT * FROM compras"""
# cursor.execute(sql_query)
# data = cursor.fetchall()
# print(data)

