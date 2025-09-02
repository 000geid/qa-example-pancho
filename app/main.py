from __future__ import annotations

from pathlib import Path
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .calculator import calculate_vegetable_grams, GRAMOS_POR_KG


BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="Calculadora de Verduras para Conejos")

# Permitir llamadas desde cualquier origen para el ejemplo simple
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_index():
    """Sirve la página HTML estática en español."""
    index_file = STATIC_DIR / "index.html"
    return FileResponse(index_file)


@app.get("/api/calcular_verduras")
def api_calcular_verduras(peso_kg: float = Query(..., gt=0, description="Peso del conejo en kilogramos")):
    gramos = calculate_vegetable_grams(peso_kg)
    return JSONResponse(
        {
            "peso_kg": peso_kg,
            "gramos": gramos,
            "regla": f"{GRAMOS_POR_KG} gramos por kg",
        }
    )


@app.get("/health")
def health():
    return {"status": "ok"}

