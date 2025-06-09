from pydantic import BaseModel, Field

class AlimentoBase(BaseModel):
    nombre: str = Field(..., example="Manzana")
    calorias: int = Field(..., example=52)

class AlimentoCreate(AlimentoBase):
    pass

class AlimentoInDB(AlimentoBase):
    id: str
