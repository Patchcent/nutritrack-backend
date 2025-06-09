from fastapi import APIRouter, HTTPException
from models.alimento import AlimentoCreate
from database import db
from bson import ObjectId

router = APIRouter()

@router.post("/", status_code=201)
async def crear_alimento(alimento: AlimentoCreate):
    # Verificar si ya existe alimento con mismo nombre
    if await db.alimentos.find_one({"nombre": alimento.nombre}):
        raise HTTPException(status_code=400, detail="Alimento ya existe")

    result = await db.alimentos.insert_one(alimento.dict())
    return {"id": str(result.inserted_id), "message": "Alimento creado"}

@router.get("/")
async def listar_alimentos():
    alimentos = []
    cursor = db.alimentos.find()
    async for alimento in cursor:
        alimento["id"] = str(alimento["_id"])
        del alimento["_id"]
        alimentos.append(alimento)
    return alimentos
