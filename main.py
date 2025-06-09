import logging
logging.basicConfig(level=logging.DEBUG)

from fastapi import FastAPI
from routes import users, alimentos, profile

app = FastAPI()

# Conectar las rutas
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(alimentos.router, prefix="/alimentos", tags=["Alimentos"])
app.include_router(profile.router, prefix="/profile", tags=["Perfil"])

@app.get("/")
async def root():
    return {"message": "NutriTrack API running"}
