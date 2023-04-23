from typing import  ClassVar
from pydantic import BaseModel
from datetime import datetime 

class SaldoInicial():
    def __init__(self):
        self.saldo:float = 100000.0

class Saldo(BaseModel):
    saldo:float
    date: ClassVar[datetime]=datetime.now()

class Compra(BaseModel):
    cantidad: float    
    date: ClassVar[datetime]=datetime.now()

class Venta(BaseModel):
    cantidad: float    
    date: ClassVar[datetime]=datetime.now()