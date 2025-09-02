from __future__ import annotations


GRAMOS_POR_KG = 100


def calculate_vegetable_grams(peso_kg: float) -> int:
    """
    Calcula la cantidad de verduras (en gramos) que debe comer un conejo
    por día según su peso en kilogramos, usando una regla simple de
    100 gramos por cada kilogramo de peso.

    - peso_kg: peso del conejo en kilogramos (debe ser > 0)
    - return: gramos de verduras como entero
    """
    if peso_kg <= 0:
        raise ValueError("El peso debe ser mayor que 0")
    gramos = round(peso_kg * GRAMOS_POR_KG)
    return int(gramos)

