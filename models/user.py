from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    nombre: str = Field(..., example="Juan Pérez")
    edad: int = Field(..., gt=0, example=30)
    sexo: str = Field(..., example="masculino")  
    peso_actual: float = Field(..., gt=0, example=72.5)
    altura: float = Field(..., gt=0, example=175.0)
    nivel_actividad: str = Field(..., example="activo")  # opciones como sedentario, moderado, etc.
