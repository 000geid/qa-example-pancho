# Calculadora de Verduras para Conejos (FastAPI + Pytest)

Aplicación mínima con FastAPI que calcula cuántos gramos de verduras debe comer un conejo según su peso, con una UI estática simple en español y una suite de tests con pytest.

Regla usada: 100 gramos por cada kilogramo de peso (ej.: 1.8 kg → 180 g al día).

## Requisitos

- Python 3.9+
- Dependencias en `requirements.txt`

## Ejecutar el servidor

1. Crear entorno e instalar dependencias:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   pip install -r requirements.txt
   ```

2. Ejecutar FastAPI con Uvicorn:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Abrir la UI:

   - Visita `http://127.0.0.1:8000/` y usa el formulario en español.
   - El endpoint de la API es `GET /api/calcular_verduras?peso_kg=<float>`.

## Ejecutar tests

```bash
pytest -q
```

Esto ilustra la ventaja de automatizar casos de prueba (p. ej., 1.25 kg → 125 g, manejo de entradas inválidas) en lugar de probar cada escenario manualmente desde la UI.

