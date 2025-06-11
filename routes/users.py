from fastapi import APIRouter, HTTPException
from models.user import UserCreate, UserLogin
from database import db
from passlib.hash import bcrypt

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    if await db.usuarios.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email ya registrado")
    hashed_password = bcrypt.hash(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password
    await db.usuarios.insert_one(user_dict)
    return {"message": "Usuario registrado con éxito"}

@router.post("/login")
async def login(user: UserLogin):
    usuario = await db.usuarios.find_one({"email": user.email})
    if not usuario or not bcrypt.verify(user.password, usuario["password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"message": "Inicio de sesión exitoso"}
