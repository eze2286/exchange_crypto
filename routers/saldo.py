
from fastapi import APIRouter
from routers.conecction_db import select_saldo_exchange


router = APIRouter()

@router.get("/saldo")
def saldo():
    saldo = select_saldo_exchange()
    if not saldo:
        saldo = 0
    return {"Su saldo actual es U$D": str(saldo)}