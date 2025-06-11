from fastapi import APIRouter, HTTPException
from models.historial_peso import PesoRegistro
from database import db  # ✅ asegurate que este importe funcione correctamente
import logging

router = APIRouter()

@router.post("/", status_code=201)
async def registrar_peso(peso_data: PesoRegistro):
    logging.debug(f"Recibido: {peso_data.dict()}")

    # Asegura que la fecha esté como string
    existe = await db.historial_peso.find_one({
        "email": peso_data.email,
        "fecha": str(peso_data.fecha)
    })
    if existe:
        raise HTTPException(status_code=400, detail="Ya existe un registro para esa fecha")

    # Inserta el nuevo peso
    result = await db.historial_peso.insert_one({
        "email": peso_data.email,
        "fecha": str(peso_data.fecha),
        "peso": peso_data.peso
    })

    return {"id": str(result.inserted_id), "message": "Peso registrado"}
@router.get("/{email}")
async def obtener_historial_peso(email: str):
    registros = []
    cursor = db.historial_peso.find({"email": email}).sort("fecha", 1)
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        registros.append(doc)
    return registros