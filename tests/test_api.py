import logging

import pytest
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_index_serves_html():
    r = client.get("/")
    assert r.status_code == 200
    assert "Calculadora de verduras para conejos" in r.text


@pytest.mark.parametrize(
    "peso_kg, esperado",
    [
        (2.0, 200),
        (1.25, 125),
        (0.75, 75),
        (1.23456789, 123),   # muchos decimales
        (1.9999, 200),       # verifica redondeo hacia arriba vs truncado
        (50.0, 5000),        # número grande
    ],
    ids=[
        "2.0kg->200g",
        "1.25kg->125g",
        "0.75kg->75g",
        "1.23456789kg->123g",
        "1.9999kg->200g",
        "50kg->5000g",
    ],
)
def test_api_calculo_valido(peso_kg, esperado):
    logging.info("Verificando API: %.2f kg -> %d g", peso_kg, esperado)
    r = client.get("/api/calcular_verduras", params={"peso_kg": peso_kg})
    assert r.status_code == 200
    data = r.json()
    logging.info("Respuesta API: %s", data)
    assert data["gramos"] == esperado


@pytest.mark.parametrize("peso_kg", [0, -1, -0.01], ids=["0kg", "-1kg", "-0.01kg"])
def test_api_calculo_invalido(peso_kg):
    logging.info("Verificando API inválido: %s kg", peso_kg)
    r = client.get("/api/calcular_verduras", params={"peso_kg": peso_kg})
    # FastAPI valida gt=0 y responde 422
    assert r.status_code == 422
