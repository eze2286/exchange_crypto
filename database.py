import sqlite3

def get_connection_to_data_base():
    con = sqlite3.connect(r'D:\Desktop\Todas mis cosas\Cursos\EXCEL\Python Senior Programmer\Exchange_Project\exchange.db')
    return con  
conexion = sqlite3.connect('exchange.db')
cursor = conexion.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS compras(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         cantidad FLOAT NOT NULL,
#         precio FLOAT NOT NULL,
#         date DATE NOT NULL
#     )
# """)

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS ventas(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         cantidad FLOAT NOT NULL,
#         precio FLOAT NOT NULL,
#         date DATE NOT NULL
#     )
# """)

# conexion.commit()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS saldo_exchange(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         saldo FLOAT NOT NULL,
#         date DATE NOT NULL
#     )
# """)

# conexion.commit()

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