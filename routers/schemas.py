from typing import Union, Optional, ClassVar
from pydantic import BaseModel
from datetime import date as date_type
from datetime import datetime 

class SaldoInicial():
    def __init__(self):
        self.saldo:float = 100000.0

class Saldo(BaseModel):
    saldo:float
    date: ClassVar[datetime]=datetime.now()

class Compra(BaseModel):
    cantidad: float
    # precio: float
    date: ClassVar[datetime]=datetime.now()

class Venta(BaseModel):
    cantidad: float
    # precio: float
    date: ClassVar[datetime]=datetime.now()