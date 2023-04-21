from fastapi import APIRouter
from routers.conecction_db import select_valued_possesion


router = APIRouter()


@router.get("/tenencia_valorizada")
def tenencia():
    tenencia = select_valued_possesion()
    if not tenencia:
        return {"No es posible realizar la transacción": "No registra tenencias a la fecha"}
    return {"Tenencia actual  ":f"{str(tenencia[0])} unidades",
            "Tenencia actual valorizada ":f"{str(tenencia[1])}"}