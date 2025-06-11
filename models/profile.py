from pydantic import BaseModel
from typing import Optional 


class UserProfile(BaseModel):
    email: str
    edad: int = 0
    peso: float = 0.0
    altura: float = 0.0
    objetivos: str = ""
    calorias_diarias: Optional[int] = 0