from pydantic import BaseModel, Field

class AlimentoBase(BaseModel):
    nombre: str = Field(..., example="Manzana")
    calorias: int = Field(..., example=52)
    proteinas: float = Field(..., example=0.3)
    grasas: float = Field(..., example=0.2)
    carbohidratos: float = Field(..., example=14)
    porcion: str = Field(..., example="100g")

class AlimentoCreate(AlimentoBase):
    pass

class AlimentoInDB(AlimentoBase):
    id: str
