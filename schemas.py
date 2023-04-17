from typing import Union, Optional
from pydantic import BaseModel
from datetime import date as date_type

class SaldoInicial():
    def __init__(self):
        self.saldo:float = 100000.0

class Saldo(BaseModel):
    saldo:float
    date: date_type

class Compra(BaseModel):
    cantidad: float
    # precio: float
    date: date_type

class Venta(BaseModel):
    cantidad: float
    # precio: float
    date: date_type
