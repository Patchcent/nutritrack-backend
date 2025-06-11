import logging
logging.basicConfig(level=logging.DEBUG)

from fastapi import FastAPI
from routes import alimentos ,users,profile,historial_peso

app = FastAPI()

# Incluye el router de alimentos con prefijo /alimentos
app.include_router(alimentos.router, prefix="/alimentos", tags=["Alimentos"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(historial_peso.router, prefix="/historial_peso", tags=["Historial de Peso"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])
@app.get("/")
async def root():
    return {"message": "NutriTrack API running"}