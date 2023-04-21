from fastapi import APIRouter
from routers.conecction_db import delete_registers_on_tables

router = APIRouter()

@router.delete("/reset_wallet")
def reset_wallet():
    reset = delete_registers_on_tables()
    return {"Operacion realizada satisfactoriamente: ": reset}