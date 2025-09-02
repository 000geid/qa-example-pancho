import logging
import pytest

from app.calculator import calculate_vegetable_grams


@pytest.mark.parametrize(
    "peso_kg, esperado",
    [
        (1.0, 100),
        (1.5, 150),
        (0.75, 75),
        (1.23456789, 123),   # muchos decimales: se redondea/trunca a 123
        (1.9999, 200),        # verifica redondeo hacia arriba vs truncado
        (50.0, 5000),         # número grande
    ],
    ids=[
        "1.0kg->100g",
        "1.5kg->150g",
        "0.75kg->75g",
        "1.23456789kg->123g",
        "1.9999kg->200g",
        "50kg->5000g",
    ],
)
def test_calculate_vegetable_grams_ok(peso_kg, esperado):
    logging.info("Aserción: %.2f kg debe dar %d g", peso_kg, esperado)
    assert calculate_vegetable_grams(peso_kg) == esperado


@pytest.mark.parametrize("peso_kg", [0, -0.1], ids=["0kg", "-0.1kg"])
def test_calculate_vegetable_grams_invalid(peso_kg):
    logging.info("Aserción inválida: %.2f kg debe lanzar ValueError", peso_kg)
    with pytest.raises(ValueError):
        calculate_vegetable_grams(peso_kg)
