from fastapi import APIRouter, HTTPException
from models.alimento import AlimentoCreate
from database import db
from typing import List

router = APIRouter()

# Ya tienes el post para 1 alimento, ahora agregamos para varios:
@router.get("/test")
async def test_endpoint():
    return {"message": "Router alimentos funcionando"}
@router.post("/bulk", status_code=201)
async def crear_varios_alimentos(alimentos: List[AlimentoCreate]):
    # Validar que no haya nombres repetidos en la lista
    nombres = [a.nombre for a in alimentos]
    if len(nombres) != len(set(nombres)):
        raise HTTPException(status_code=400, detail="Nombres duplicados en la lista")

    # Validar que ninguno exista ya en la base
    for nombre in nombres:
        if await db.alimentos.find_one({"nombre": nombre}):
            raise HTTPException(status_code=400, detail=f"Alimento '{nombre}' ya existe")

    # Insertar todos los alimentos
    docs = [a.dict() for a in alimentos]
    result = await db.alimentos.insert_many(docs)

    return {"inserted_ids": [str(id) for id in result.inserted_ids], "message": "Alimentos creados"}

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
