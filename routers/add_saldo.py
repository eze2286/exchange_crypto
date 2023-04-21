from fastapi import APIRouter
from routers.conecction_db import add_saldo_database
from routers.schemas import Saldo


router = APIRouter()

@router.post("/saldo")
def add_saldo(saldo:Saldo):
    saldo_exch = add_saldo_database(saldo_exchange = saldo)
    return {"Transaccion satisfactoria":f"Se cargaron correctamente U$S {str(saldo.saldo)} a su billetera"}