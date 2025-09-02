import logging
import pytest

from app.calculator import calculate_vegetable_grams


@pytest.mark.parametrize(
    "peso_kg, esperado",
    [(1.0, 100), (1.5, 150), (0.75, 75)],
    ids=["1.0kg->100g", "1.5kg->150g", "0.75kg->75g"],
)
def test_calculate_vegetable_grams_ok(peso_kg, esperado):
    logging.info("Asserción: %.2f kg debe dar %d g", peso_kg, esperado)
    assert calculate_vegetable_grams(peso_kg) == esperado


@pytest.mark.parametrize("peso_kg", [0, -0.1], ids=["0kg", "-0.1kg"])
def test_calculate_vegetable_grams_invalid(peso_kg):
    logging.info("Asserción inválida: %.2f kg debe lanzar ValueError", peso_kg)
    with pytest.raises(ValueError):
        calculate_vegetable_grams(peso_kg)
