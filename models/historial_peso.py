from pydantic import BaseModel
from datetime import date

class PesoRegistro(BaseModel):
    email: str
    fecha: date  # formato ISO 8601: "2024-06-10"
    peso: float  # en kilogramos
