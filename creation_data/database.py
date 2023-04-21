# import pymysql
# import os 
# def get_connection_to_data_base():
#     conn=pymysql.connect(
#     host = 'exchange-db.cjgfmaah7lau.us-east-1.rds.amazonaws.com',
#     user =  'admin',
#     password = os.getenv('dbpassword')
#     )



# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS compras(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         cantidad FLOAT NOT NULL,
#         date DATE NOT NULL
#     )
# """)

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS ventas(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         cantidad FLOAT NOT NULL,
#         date DATE NOT NULL
#     )
# """)

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS saldo_exchange(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         saldo FLOAT NOT NULL,
#         date DATE NOT NULL
#     )
# """)

# conexion.commit()