from fastapi.testclient import TestClient
from fastapi import status
from main import app
from routers.external_data import close_price
from routers.conecction_db import select_saldo_exchange

client = TestClient(app)

def test_compra():
    response = client.post("/compra",
                           json={
                                "cantidad": 1.0
                                })    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
                            "Success operation": f"se realizó la compra de 1.0 unidades"
                            }

def test_saldo_disponible_para_compra():
    cierre = close_price
    saldo = select_saldo_exchange()
    response = client.post("/compra",
                           json={
                                "cantidad": 10000 # cantidad mayor a lo disponible para probar
                                })
    monto_compra = float(10000 * cierre)   
    assert response.status_code == status.HTTP_406_NOT_ACCEPTABLE
    detail=f"error: Saldo insuficiente, su saldo es {saldo} y el monto de compra es {monto_compra}"
    assert response.json() == {'detail':detail}

def test_cantidad_compra_equal_0():
    response = client.post("/compra",
                           json={
                                "cantidad": 0
                                })    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    detail="La cantidad comprada debe ser mayor a 0"
    assert response.json() == {'detail':detail}