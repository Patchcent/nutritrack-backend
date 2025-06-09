from fastapi import APIRouter, HTTPException
from models.profile import UserProfile
from database import db

router = APIRouter()

@router.get("/{email}", response_model=UserProfile)
async def obtener_perfil(email: str):
    perfil = await db.perfiles.find_one({"email": email})
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    perfil.pop("_id", None)
    return perfil

@router.post("/{email}")
async def crear_o_actualizar_perfil(email: str, perfil: UserProfile):
    perfil_dict = perfil.dict()
    perfil_dict["email"] = email
    await db.perfiles.update_one(
        {"email": email},
        {"$set": perfil_dict},
        upsert=True
    )
    return {"message": "Perfil actualizado"}
