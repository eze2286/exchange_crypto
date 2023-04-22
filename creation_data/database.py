import pymysql
import os 
def get_connection_to_data_base():
    conn=pymysql.connect(
    host = 'exchange-db.cjgfmaah7lau.us-east-1.rds.amazonaws.com',
    user =  'admin',
    password = os.getenv('dbpassword')        
    )
    return conn

# conexion = get_connection_to_data_base()
# cursor=conexion.cursor()
# sql_use = """USE exchange"""
# cursor.execute(sql_use)
# sql_query = """DROP TABLE saldo_exchange"""
# cursor.execute(sql_query)
# sql_query = """DROP TABLE compras"""
# cursor.execute(sql_query)
# sql_query = """DROP TABLE ventas"""
# cursor.execute(sql_query)
# conexion.commit()
# conexion.close()


# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS compras(
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         precio FLOAT NOT NULL,
#         cantidad FLOAT NOT NULL,
#         date DATETIME NOT NULL
#     )
# """)

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS ventas(
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         precio FLOAT NOT NULL,
#         cantidad FLOAT NOT NULL,
#         date DATETIME NOT NULL
#     )
# """)

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS saldo_exchange(
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         saldo FLOAT NOT NULL,
#         date DATETIME NOT NULL
#     )
# """)

# conexion.commit()
# conexion.close()