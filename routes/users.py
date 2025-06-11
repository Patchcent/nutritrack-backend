from fastapi import APIRouter, HTTPException
from models.user import UserCreate
from database import db
from security import hash_password  # 👈 Asegúrate de importar esto

router = APIRouter()

@router.post("/registro")
async def registrar_usuario(usuario: UserCreate):
    # Verifica si ya existe el usuario
    if await db.users.find_one({"email": usuario.email}):
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Hashear la contraseña
    usuario_dict = usuario.dict()
    usuario_dict["password"] = hash_password(usuario.password)

    # Insertar en la base
    result = await db.users.insert_one(usuario_dict)
    return {"id": str(result.inserted_id), "message": "Usuario registrado"}
