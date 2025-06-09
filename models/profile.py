from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    altura: float = Field(..., example=1.75)  # metros
    peso: float = Field(..., example=70.5)    # kilogramos
    calorias_diarias: int = Field(..., example=2000)
