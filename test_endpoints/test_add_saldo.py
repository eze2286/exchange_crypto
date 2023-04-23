from fastapi.testclient import TestClient
from fastapi import status
from routers.external_data import close_price
from main import app

client = TestClient(app)

def test_add_saldo():
    response = client.post("/saldo",
                           json={
                                "saldo": 1000.0
                                })    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
                            "Transaccion satisfactoria": "Se cargaron correctamente U$S 1000.0 a su billetera"
                            }

def test_add_saldo_equal_0():
    response = client.post("/saldo",
                           json={
                                "saldo": 0
                                })    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    detail="El saldo a ingresar debe ser mayor a 0"
    assert response.json() == {'detail':detail}