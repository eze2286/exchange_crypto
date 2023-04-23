from fastapi.testclient import TestClient
from fastapi import status
from main import app
from routers.conecction_db import select_quantity_cripto

client = TestClient(app)

def test_venta():
    response = client.post("/venta",
                           json={
                                "cantidad": 1.0
                                })    
    assert response.status_code == status.HTTP_201_CREATED

def test_cantidad_disponible_para_venta():   
    response = client.post("/venta",
                           json={
                                "cantidad": 10000 # cantidad mayor a lo disponible para probar
                                })
    cantidad = select_quantity_cripto()
    assert response.status_code == status.HTTP_406_NOT_ACCEPTABLE
    detail=f"error : Cantidad disponible: {str(cantidad)} - Cantidad solicitada: 10000.0"
    assert response.json() == {'detail':detail}

def test_cantidad_venta_equal_0():
    response = client.post("/venta",
                           json={
                                "cantidad": 0
                                })    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    detail="La cantidad vendida debe ser mayor a 0"
    assert response.json() == {'detail':detail}