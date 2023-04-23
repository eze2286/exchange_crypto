from fastapi.testclient import TestClient
from fastapi import status
from routers.external_data import close_price
from main import app

client = TestClient(app)

def test_close_price():
    response = client.get("/cierre_diario")
    cierre = float(close_price)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"El precio actual es de U$S":cierre}

def test_bad_close_price():
    response = client.get("/cierre_diario")
    cierre = float(close_price)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"El precio actual es de U$S":0.00}

